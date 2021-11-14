from threading import Thread, Lock
from time import time, sleep
import random
import logging


logging.basicConfig(level=logging.DEBUG)


lock = Lock()
start = time()


def train(arrive_time, transit_time, index):
    print("Поїзд {} прибуває через {:.4f} секунд і проходить "
          "ділянку за {:.4f} секунд"
          .format(index, arrive_time, transit_time))
    sleep(arrive_time)
    logging.debug("Поїзд {} прибув до ділянки".format(index))
    # lock.acquire()
    with lock:
        logging.debug("Поїзд {} почав проходити ділянку".format(index))
        sleep(transit_time)
    # lock.release()
    logging.debug("Поїзд {} пройшов ділянку".format(index))
    print("Поїзд {} пройшов ділянку. Повний час подорожі {:.4f}"
          .format(index, time() - start))


def next_train(t1, t2, t3, t4, index):
    transit_time = random.random() * (t2 - t1) + t1
    arrive_time = random.random() * (t4 - t3) + t3
    th = Thread(target=train, args=(arrive_time, transit_time, index))
    th.start()
    return th


if __name__ == '__main__':
    n = 10
    t1 = 1
    t2 = 5
    t3 = 0
    t4 = 30

    ths = []
    for i in range(n):
        ths.append(next_train(t1, t2, t3, t4, i))
    for i in range(n):
        ths[i].join()
