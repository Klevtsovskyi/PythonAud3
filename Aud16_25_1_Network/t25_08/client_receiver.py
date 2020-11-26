

import socket
import os


class ClientReceiver:

    def __init__(self, host, port, dirname):
        self.dirname = dirname
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        self.socket = socket.socket()
        self.socket.connect((host, port))
        self.rfile = self.socket.makefile("rb", 0)
        self.wfile = self.socket.makefile("wb", 0)
        print("Успішно під'єднано до сервера")
        self.run()
        self.finish()

    def run(self):
        self._send("/receiver")
        while True:
            message = self._readline()
            if message == "/start":
                self._receive_file()
            elif message == "/end":
                self._send("/end")
                break

    def _receive_file(self):
        filename = self._readline()
        f = open(os.path.join(self.dirname, filename), "wb")
        print("Отриманання файла", filename)
        while True:
            size = int(self._readline()[5:])
            if size == 0:
                break
            b = self.rfile.read(size)
            f.write(b)
        f.close()
        print("Завершено передачу файла", filename)

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
    ClientReceiver(HOST, PORT, "rec")
