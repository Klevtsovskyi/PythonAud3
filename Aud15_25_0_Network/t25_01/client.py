

import socket


def run_client(host, port, inp, out):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print("Під'єднано до сервера", host)
    input()
    finp = open(inp)
    fout = open(out, "w")
    for line in finp:
        out_bytes = bytes(line, encoding="utf-8")
        s.sendall(out_bytes)
        print("Дані відправлено на сервер:", out_bytes)
        inp_bytes = s.recv(1024)
        print("Дані отримано від сервера:", inp_bytes)
        inp_string = str(inp_bytes, encoding="utf-8")
        fout.write(inp_string)
    s.sendall(b"")
    finp.close()
    fout.close()
    s.close()
    print("Клієнт завершив роботу")


HOST = "127.0.0.1"
PORT = 20000


if __name__ == '__main__':
    run_client(HOST, PORT, "input.txt", "output.txt")
