import os
import socketserver


class RequestHandler(socketserver.StreamRequestHandler):

    def handle(self) -> None:
        print(f"Під`єднано {self.client_address}")
        while True:
            # Отримуємо ім`я файлу від клієнта
            filename = self._receive()
            # Якщо ім`я файлу відсутнє, розірвуємо зв`язок з клієнтом
            if not filename:
                break

            print(f"Отримано ім`я файлу: {filename}")
            f = open(os.path.join(DIR, filename), "wb")
            # Зберігаємо файл на сервері по частинам
            while True:
                # Отримуємо розмір частини від клієнта
                size = int(self._receive())
                # Якщо розмір дорівнює нулю, передача завершена
                if size == 0:
                    break
                # Отримуємо частину від клієнта
                b = self.rfile.read(size)
                # Додаємо до файлу частину
                f.write(b)

            f.close()
            print(f"Запис файлу {filename} завершено")

    def finish(self) -> None:
        print(f"Роз`єднано {self.client_address}")
        self.request.close()

    def _receive(self) -> str:
        line = str(self.rfile.readline().rstrip(), encoding="utf-8")
        print(f"Отримано: {line}")
        return line

    def _send(self, message) -> None:
        self.wfile.write(bytes(message + "\n", encoding="utf-8"))
        print(f"Відправлено: {message}")


DIR = "data"
HOST = ""
PORT = 10000


if __name__ == "__main__":
    if not os.path.isdir(DIR):
        os.mkdir(DIR)

    print(f"Сервер запущено на {HOST if HOST else '127.0.0.1'}:{PORT}")
    server = socketserver.TCPServer((HOST, PORT), RequestHandler)
    server.handle_request()
