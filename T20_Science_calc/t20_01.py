import numpy as np
import matplotlib.pyplot as plt


def func01(n):
    return (n * 3 / 2 * (1 - 1/pow(3, n+1)) * (n - 3) * pow(n, 1/n) /
            (2*n*n + 5))


def gety(f, x):
    """ Повертає масив значень функції f(x)"""
    n = x.size
    y = np.zeros(n)
    for i in range(n):
        y[i] = f(int(x[i]))
    return y


def func01_gen(n, step):  # а
    s = 1
    p = 1
    for _ in range(n):
        p *= 1/3
        s += p
    while True:
        yield n * s * (n - 3) * pow(n, 1/n) / (2*n*n + 5)
        for _ in range(step):
            p *= 1/3
            s += p
        n += step


def vect(fgen, a, b, step=1):
    """ Повертає масиви значень аргументів (x) та функції (f(x))
        по розбиттю піввідрізка [a, b) з кроком step
    """
    x = np.arange(a, b, step)
    y = np.zeros_like(x, dtype=float)
    gen = fgen(a, step)
    for i in range(x.size):
        y[i] = next(gen)
    return x, y


def plot_seq(x, y, b=None, eps=0.01, forall=True):
    """ Візуалізує послідовність y = f(x)"""
    if b is None:
        # Якщо границя послідовності невідома, будуємо послідовнісь
        # та повертаємо її останній елемент за розбиттям
        plt.plot(x, y, ".b")
        return y[-1]
    else:
        # Якщо границя послідовності відома,
        # перевіряємо, чи потрапляють останні елементи у проміжок

        # Номер першого елемента послідовності, який потрапив
        # у проміжок разом з наступними
        k = -1
        # Чи потрапив попередній елемент у проміжок
        prev = False
        # Перевіряємо, чи потрапляють у проміжок елементи послідовності
        for i in range(y.size):
            if abs(y[i] - b) < eps:
                if not prev:
                    k = i
                    prev = True
            else:
                prev = False

        # Якщо останній елемент послідовності не потрапив у проміжок,
        # повертаємо None
        if not prev:
            return

        # Якщо forall=True, будуємо на графіку всі елементи,
        # інакше тільки ті, що потрапили в проміжок
        begin = 0 if forall else k

        # Будуємо графіки
        plt.plot(x[begin:], y[begin:], ".b")
        plt.plot(np.array((x[begin], x[-1])), np.array((b, b)), "-r")
        plt.plot(np.array((x[begin], x[-1])), np.array((b - eps, b - eps)), "--g")
        plt.plot(np.array((x[begin], x[-1])), np.array((b + eps, b + eps)), "--g")
        # Підписуємо вісі
        plt.xlabel("n")
        plt.ylabel("a(n)")
        # Встановлюємо зріз ділянки, яка показує графік
        plt.axis([x[begin], x[-1], b - eps*2, b + eps*2])
        # Повертаємо номер останнього елемента послідовності,
        # який потрапив у проміжок за даним розбиттям
        return x[k]


if __name__ == "__main__":
    t = (1, 200, 1)  # параметри розбиття: (початок, кінець, крок)
    # x = np.arange(*t)
    # y = gety(func01, x)
    x, y = vect(func01_gen, *t)
    # print(x, y)
    # print(plot_seq(x, y))
    b = 0.75  # границя
    eps = 0.01
    print(plot_seq(x, y, b, eps, True))
    plt.show()
