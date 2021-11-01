import os
import sys
import datetime


def create_log():
    log_dir = os.path.join(sys.path[0], "logs")
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    now = datetime.datetime.now()
    filename = now.strftime("%Y%m%d_%H%M%S.log")
    with open(os.path.join(log_dir, filename), "w", encoding="utf-8") as out:
        with open("input.txt", "r", encoding="utf-8") as inp:
            out.write(inp.read())


if __name__ == "__main__":
    create_log()
