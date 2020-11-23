

import socketserver
import socket
import os


DIR = "server_data"


class RequestHandler(socketserver.StreamRequestHandler):

    def handle(self) -> None:
        if not os.path.exists(DIR):
            os.mkdir(DIR)
        print("Під'єднано", self.client_address)
        try:
            while True:
                filename = self._readline()
                if not filename:
                    break
                print("Отримано ім'я файлу:", filename)
                f = open(os.path.join(DIR, filename), "wb")
                while True:
                    size = int(self._readline())
                    if size == 0:
                        break
                    b = self.rfile.read(size)
                    f.write(b)
                f.close()
                print("Запис файлу завершено")
        except socket.error as e:
            print(e)

    def finish(self) -> None:
        print("Роз'єднано", self.client_address)
        self.request.shutdown(socket.SHUT_RDWR)
        self.request.close()

    def _readline(self):
        line = str(self.rfile.readline().strip(), encoding="utf-8")
        print("Отримано", line)
        return line

    def _send(self, message):
        print("Відправлено", message)
        self.wfile.write(bytes(message + "\n", encoding="utf-8"))


HOST = ""
PORT = 20000


if __name__ == '__main__':
    print("=== Сервер запущено ===")
    socketserver.TCPServer((HOST, PORT), RequestHandler).serve_forever()
