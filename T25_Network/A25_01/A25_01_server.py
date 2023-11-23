import socket


def run_server(host, port):
    s = socket.socket()
    s.bind((host, port))
    s.listen()
    print(f"Сервер запущено на {host if host else '127.0.0.1'}:{port}")
    conn, address = s.accept()
    print(f"Під`єднано {address}")

    # Блок обміну даними
    i = 0
    while True:
        i += 1
        inp_b = conn.recv(1024)
        print(f"Отримано від клієнта: {inp_b}")
        # Якщо клієнт присилає пустий рядок байтів, завершуємо зв`язок
        if not inp_b:
            break
        inp_s = str(inp_b, encoding="utf-8")
        out_s = f"{i} {inp_s}"
        out_b = bytes(out_s, encoding="utf-8")
        conn.sendall(out_b)
        print(f"Відправлено клієнту: {out_b}")

    conn.close()
    s.close()
    print("Сервер звершив роботу")


HOST = ""
PORT = 10000


if __name__ == "__main__":
    run_server(HOST, PORT)
