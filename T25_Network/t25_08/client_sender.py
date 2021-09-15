

import socket


class ClientSender:

    def __init__(self, host, port):
        self.socket = socket.socket()
        self.socket.connect((host, port))
        self.rfile = self.socket.makefile("rb", 0)
        self.wfile = self.socket.makefile("wb", 0)
        print("Успішно під'єднано до сервера")
        self.run()
        self.finish()

    def run(self):
        self._send("/sender")
        while True:
            message = self._readline()
            if message == "/start":
                while True:
                    filename = input("Ім'я файла")
                    if filename:
                        self._send_file(filename)
                    else:
                        self._send("/t/end")
                        self._send("/end")
                        return

    def _send_file(self, filename):
        try:
            f = open(filename, "rb")
            self._send("/t/start")
            print("Відправка файла", filename)
            self._send("/t" + filename)
            while True:
                b = f.read(1024)
                self._send("/t/size" + str(len(b)))
                if b:
                    self.wfile.write(b)
                else:
                    print("Завершено передачу файла", filename)
                    break
        except FileNotFoundError:
            print("Заданого файлу не існує")

    def finish(self):
        self.socket.close()
        print("Зв'язок з сервером розірвано")

    def _readline(self):
        line = str(self.rfile.readline().strip(), encoding="utf-8")
        print("Отримано:", line)
        return line

    def _send(self, message):
        print("Відправлено:", message)
        self.wfile.write(bytes(message + "\n", encoding="utf-8"))


HOST = "127.0.0.1"
PORT = 20002


if __name__ == '__main__':
    ClientSender(HOST, PORT)
