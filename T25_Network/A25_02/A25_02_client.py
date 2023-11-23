import os
import socket


class Client:

    def __init__(self, host, port):
        self.socket = socket.socket()
        self.socket.connect((host, port))

        # Файл для отримання даних
        self.rfile = self.socket.makefile("rb", 0)
        # Файл для відправки даних
        self.wfile = self.socket.makefile("wb", 0)

        print(f"Під`єднано до сервера {host}:{port}")
        self.run()
        self.finish()

    def run(self):
        while True:
            filepath = input("Введіть ім`я файлу або пустий рядок для зупинки: ")
            # Якщо рядок пустий, насилаємо серверу інформацію про завершення зв`язку
            if not filepath:
                self._send("")
                break

            if not os.path.isfile(filepath):
                print("Заданого файлу не існує")
                continue

            f = open(filepath, "rb")
            filename = os.path.basename(filepath)
            # Відправляємо ім`я файлу та починаємо його передачу по частинам
            self._send(filename)
            while True:
                b = f.read(1024)  # Читаємо частину файлу
                size = len(b)     # Знаходимо розмір частини
                # Відправляємо на сервер розмір частини
                self._send(str(size))
                if size == 0:
                    # Якщо розмір нуль, файл передано
                    print(f"Завершено передачу файлу: {filepath}")
                    break
                else:
                    # Інакше передаємо частину
                    self.wfile.write(b)

            f.close()

    def finish(self):
        self.socket.close()
        print("Зв`язок з сервером розірвано")

    def _receive(self) -> str:
        line = str(self.rfile.readline().rstrip(), encoding="utf-8")
        print(f"Отримано: {line}")
        return line

    def _send(self, message) -> None:
        self.wfile.write(bytes(message + "\n", encoding="utf-8"))
        print(f"Відправлено: {message}")


HOST = "127.0.0.1"
PORT = 10000


if __name__ == "__main__":
    Client(HOST, PORT)

