from abc import ABCMeta, abstractmethod
import socket
import logging

# Щоб відслідковувати роботу програм, зніміть закоментований рядок нижче
# logging.basicConfig(level=logging.DEBUG)

# Перелік можливих команд (після команди може бути задано параметр)
CLIENT = "CLIENT"      # Працювати як 1 або 2 клієнт (інше - невідомий клієнт)
BEGIN = "BEGIN"        # Розпочати обмін між клієнтами
MESSAGE = "MESSAGE"    # Передати програмі повідомлення
QUESTION = "QUESTION"  # Надіслати рядок на обробку клієнту 1
ANSWER = "ANSWER"      # Результат обробки рядка клієнтом 1
END = "END"            # Завершити роботу і роз`єднатися


class BaseDataExchangeProtocol:
    """ Інтерфейс для додавання функціоналу обміну даними в мережі."""

    def receive(self) -> (str, str):
        cmd, param = self.rfile.readline().decode("utf-8").rstrip("\n\r").split(" ", maxsplit=1)
        logging.debug(f"Отримано: {cmd} {param}")
        return cmd, param

    def send(self, cmd: str, param="") -> None:
        self.wfile.write(f"{cmd} {param}\n".encode("utf-8"))
        logging.debug(f"Відправлено: {cmd} {param}")


class BaseClient(BaseDataExchangeProtocol, metaclass=ABCMeta):

    def __init__(self, host, port):
        self.socket = socket.socket()
        self.socket.connect((host, port))

        self.rfile = self.socket.makefile("rb", 0)
        self.wfile = self.socket.makefile("wb", 0)

        print(f"Під`єднано до сервера {host}:{port}")
        self.run()
        self.finish()

    @abstractmethod
    def run(self) -> None:
        pass

    def finish(self) -> None:
        print("Зв`язок з сервером розірвано")
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
