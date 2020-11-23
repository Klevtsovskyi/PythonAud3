

from t21_05 import change_dates
import socket


def run_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    print("=== Сервер запущено ===")
    while True:
        conn, address = s.accept()
        print("Під'єднано", address)
        try:
            while True:
                inp_bytes = conn.recv(1024)
                if not inp_bytes:
                    break
                print("Отримано від клієнта:", inp_bytes)
                inp_string = str(inp_bytes, encoding="utf-8")
                out_string = change_dates(inp_string, 2)
                out_bytes = bytes(out_string, encoding="utf-8")
                conn.sendall(out_bytes)
                print("Надіслано клієнту:", out_bytes)
        except socket.error as e:
            print(e)
        finally:
            conn.close()
            print("Розірвано зв'язок з", address)

    s.close()
    print("Сервер завершив роботу")


HOST = ""
PORT = 20000


if __name__ == '__main__':
    run_server(HOST, PORT)
