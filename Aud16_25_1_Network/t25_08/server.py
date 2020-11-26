

import socket
import socketserver


class FileSharingServer(socketserver.ThreadingTCPServer):

    def __init__(self, server_address, handler):
        super().__init__(server_address, handler)
        self.sender = None
        self.receiver = None


class RequestHandler(socketserver.StreamRequestHandler):

    def handle(self) -> None:
        print("Під'єднано", self.client_address)
        name = self._readline()
        if name == "/sender":
            self.server.sender = (self.rfile, self.wfile)
        elif name == "/receiver":
            self.server.receiver = (self.rfile, self.wfile)

        if self.server.sender and self.server.receiver:
            self._send_to_sender("/start")

        done = False
        while not done:
            message = self._readline()
            if message.startswith("/t"):
                message = message[2:]
                self._send_to_receiver(message)
                if message.startswith("/size"):
                    size = int(message[5:])
                    b = self.server.sender[0].read(size)
                    self.server.receiver[1].write(b)
            elif message == "/end":
                done = True

    def finish(self) -> None:
        print("Роз'єднано з", self.client_address)
        self.request.shutdown(socket.SHUT_RDWR)
        self.request.close()

    def _readline(self):
        line = str(self.rfile.readline().strip(), encoding="utf-8")
        return line

    def _send(self, message):
        self.wfile.write(bytes(message + "\n", encoding="utf-8"))

    def _send_to_sender(self, message):
        wfile = self.server.sender[1]
        wfile.write(bytes(message + "\n", encoding="utf-8"))

    def _send_to_receiver(self, message):
        wfile = self.server.receiver[1]
        wfile.write(bytes(message + "\n", encoding="utf-8"))


HOST = ""
PORT = 20002


if __name__ == '__main__':
    print("=== Сервер запущено ===")
    FileSharingServer((HOST, PORT), RequestHandler).serve_forever()
