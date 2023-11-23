from A25_03_protocol import *
import socketserver


class Server(socketserver.ThreadingTCPServer):

    def __init__(self, client_address, handler):
        self.client = {0: None, 1: None, 2: None}
        super().__init__(client_address, handler)


class RequestHandler(socketserver.StreamRequestHandler, BaseDataExchangeProtocol):

    def __init__(self, request, client_address, server):
        self.no = 0
        super().__init__(request, client_address, server)

    def no_client(self, i) -> bool:
        return self.server.client[i] is None

    def set_client(self, i, client) -> None:
        self.no = i
        self.server.client[i] = client

    def handle(self) -> None:
        print(f"Під`єднано {self.client_address}")
        try:
            cmd, param = self.receive()
            i = int(param)
            if cmd == CLIENT and self.no_client(i):
                self.set_client(i, self)
                print(f"Під`єднано {self.client_address} як клієнта {i}")
            else:
                self.send(END, f"Клієнта {i} вже під`єднано")
                return

            if self.no_client(1):
                self.send(MESSAGE, "Очікуємо на клієнта 1")
            if self.no_client(2):
                self.send(MESSAGE, "Очікуємо на клієнта 2")
            if not self.no_client(1) and not self.no_client(2):
                self.server.client[1].send(BEGIN)

            while True:
                cmd, param = self.receive()
                if cmd == BEGIN:
                    self.server.client[2].send(BEGIN)
                elif cmd == QUESTION:
                    self.server.client[2].send(QUESTION, param)
                elif cmd == ANSWER:
                    self.server.client[1].send(ANSWER, param)
                elif cmd == END:
                    return

        except Exception as e:
            print(e)

    def finish(self) -> None:
        print(f"Роз`єднано {self.client_address} як клієнта {self.no}")
        self.set_client(self.no, None)
        self.request.shutdown(socket.SHUT_RDWR)
        self.request.close()


HOST = ""
PORT = 20003


if __name__ == "__main__":
    print(f"Сервер запущено на {HOST if HOST else '127.0.0.1'}:{PORT}")
    tcp_server = Server((HOST, PORT), RequestHandler)
    tcp_server.serve_forever()
