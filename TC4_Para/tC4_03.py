from threading import Thread
from queue import Queue
from time import time, sleep
import random
import logging


logging.basicConfig(level=logging.DEBUG)


q = Queue()
start = time()


def put(n, p_time, fixed=False):
    for i in range(n):
        t = p_time if fixed else random.random() * (p_time - 1) + 1
        sleep(t)
        message = f"ПОВІДОМЛЕННЯ {i} (створено о {time() - start:.4f})"
        logging.debug(f"В чергу додано {message}, яке створювалось {t:.4f} секунд")
        q.put(message)


def get(n, p_time, fixed=False):
    for i in range(n):
        t = p_time if fixed else random.random() * (p_time - 1) + 1
        message = q.get()
        logging.debug(f"З черги отримано {message}, яке буде оброблятись {t:.4f} секунд")
        sleep(t)
        print(f"\"{message}\" оброблене на {time() - start:.4f} секунді")


if __name__ == "__main__":
    n = 10
    t1 = 2
    t2 = 4

    th1 = Thread(target=put, args=(n, t1))
    th2 = Thread(target=get, args=(n, t2))
    th1.start()
    th2.start()

    th1.join()
    th2.join()
