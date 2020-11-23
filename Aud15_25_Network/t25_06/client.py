

import socket


class Client:

    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.rfile = self.socket.makefile("rb", 0)
        self.wfile = self.socket.makefile("wb", 0)
        print("Успішно під'єднано до сервера")
        self.run()

    def run(self):
        while True:
            filename = input("Введіть ім'я файлу: ")
            if not filename:
                self._send("")
                break
            try:
                f = open(filename, "rb")
                self._send(filename)
                while True:
                    b = f.read(1024)
                    self._send(str(len(b)))
                    if b:
                        self.wfile.write(b)
                    else:
                        print("Завершено передачу файлу", filename)
                        break
            except FileNotFoundError:
                print("Заданого файлу не існує")

        self.socket.close()
        print("Зв'язок з сервером розірвано")

    def _readline(self):
        line = str(self.rfile.readline().strip(), encoding="utf-8")
        print("Отримано", line)
        return line

    def _send(self, message):
        print("Відправлено", message)
        self.wfile.write(bytes(message + "\n", encoding="utf-8"))


HOST = "127.0.0.1"
PORT = 20000


if __name__ == '__main__':
    Client(HOST, PORT)
