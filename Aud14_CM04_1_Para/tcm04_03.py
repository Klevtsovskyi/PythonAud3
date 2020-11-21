

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
        message = ("ПОВІДОМЛЕННЯ {}: створено в {:.4f}"
                   .format(i, time() - start))
        logging.debug("В чергу додано повідомлення {} через {:.4f} секунд"
                      .format(message, t))
        q.put(message)


def get(n, p_time, fixed=False):
    for i in range(n):
        t = p_time if fixed else random.random() * (p_time - 1) + 1
        message = q.get()
        logging.debug("З черги вийнято повідомлення {}, яке буде "
                      "оброблятись {:.4f} секунд"
                      .format(message, t))
        sleep(t)
        print(message, "оброблене через {:.4f} після старту"
              .format(time() - start))


if __name__ == '__main__':
    n = 10
    t1 = 2
    t2 = 4

    th1 = Thread(target=put, args=(n, t1))
    th2 = Thread(target=get, args=(n, t2))
    th1.start()
    th2.start()

    th1.join()
    th2.join()
