from threading import Thread
from time import sleep
import logging


logging.basicConfig(level=logging.DEBUG)


class ThreadWithException(Thread):

    def __init__(self, target=None, args=(), kwargs=()):
        self._func = target
        self._f_args = args
        self._f_kwargs = kwargs if kwargs else {}
        self._exception = None
        self._result = None

        super().__init__(daemon=True)

    def run(self):
        try:
            self._result = self._func(*self._f_args, **self._f_kwargs)
        except Exception as e:
            self._exception = e

    def get_result(self):
        return self._result

    def get_exception(self):
        return self._exception


def fact(n):
    result = 1
    for i in range(1, n + 1):
        logging.debug("Обчислення нерекурсивного факторіалу для {}"
                      .format(i))
        result *= i
        logging.debug("Нерекурсивний факторіал для {} дорівнює {}"
                      .format(i, result))
        sleep(0)
    return result


def fact_rec(n):
    logging.debug("Обчислення рекурсивного факторіалу для {}"
                  .format(n))
    if n == 0:
        result = 1
    else:
        result = n * fact_rec(n - 1)
    logging.debug("Нерекурсивний факторіал для {} дорівнює {}"
                  .format(n, result))
    sleep(0)
    return result


if __name__ == '__main__':
    n = 40

    th1 = ThreadWithException(target=fact, args=(n, ))
    th2 = ThreadWithException(target=fact_rec, args=(n, ))
    th1.start()
    th2.start()

    for k in range(10):
        logging.debug("Tick {}".format(k))
        sleep(0)

    th1.join()
    th2.join()

    if th1.get_exception():
        print("Отримано виключення в потоці 1: ", th1.get_exception())
    else:
        print("Потік 1 завершився успішно: ", th1.get_result())

    if th2.get_exception():
        print("Отримано виключення в потоці 2: ", th2.get_exception())
    else:
        print("Потік 2 завершився успішно: ", th2.get_result())
