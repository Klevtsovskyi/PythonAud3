from A25_03_protocol import *


class Client1(BaseClient):

    def run(self) -> None:
        try:
            self.send(CLIENT, 2)
            i = 0
            while True:
                cmd, param = self.receive()
                if cmd == BEGIN:
                    i = 0
                elif cmd == QUESTION:
                    i += 1
                    self.send(ANSWER, f"{i:4} {param}")
                elif cmd == MESSAGE:
                    print(param)
                elif cmd == END:
                    print(param)
                    return

        except Exception as e:
            print(e)


HOST = "127.0.0.1"
PORT = 20003

if __name__ == "__main__":
    Client1(HOST, PORT)
