from A25_03_protocol import *
import os.path


def input_files():
    while True:
        try:
            inp = input("Введіть назву файлу для считування: ")
            out = input("Введіть назву файлу для збереження: ")
            inp = os.path.abspath(inp)
            out = os.path.abspath(out)
            finp = open(inp, "r", encoding="utf-8")
            fout = open(out, "w", encoding="utf-8")
            break
        except OSError:
            print("Помилка при роботі з файлами. Повторіть введення")
    return finp, fout


class Client2(BaseClient):

    def run(self) -> None:
        try:
            self.send(CLIENT, 1)
            while True:
                cmd, param = self.receive()
                if cmd == BEGIN:
                    print("Розпочинається робота")
                    break
                elif cmd == MESSAGE:
                    print(param)
                elif cmd == END:
                    print(param)
                    return

            # Розпочинаємо роботу
            while True:
                mode = input(
                    "Режими роботи [0 - розпочати, 1 - завершити]: "
                ).strip()
                if mode == "1":
                    self.send(END)
                    return
                elif mode == "0":
                    finp, fout = input_files()
                    self.send(BEGIN)
                    for line in finp:
                        self.send(QUESTION, line.rstrip("\n\r"))
                        cmd, param = self.receive()
                        fout.write(param + "\n")
                    finp.close()
                    fout.close()
                else:
                    print("Невідома команда")

        except Exception as e:
            print(e)


HOST = "127.0.0.1"
PORT = 20003

if __name__ == "__main__":
    Client2(HOST, PORT)
