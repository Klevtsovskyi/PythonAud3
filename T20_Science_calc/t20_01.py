import numpy as np
import matplotlib.pyplot as plt


def func01(n):
    return 3 / 2 * (1 - 1/np.power(3, n+1)) * (n - 3) * np.power(n, 1/n) / (2.0 * n + 5 / n)


def gety(f, x):
    """ Повертає масив значень функції f(x) (альтернатва векторизації)"""
    n = x.size
    y = np.zeros(n)
    for i in range(n):
        y[i] = f(x[i])
    return y


def plot_seq(x, y, b=None, eps=0.01, forall=True):
    """ Візуалізує послідовність y = f(x)"""
    plt.figure(figsize=(12, 9))
    # Підписуємо вісі
    plt.xlabel("n")
    plt.ylabel("a(n)")
    if b is None:
        # Якщо границя послідовності невідома, будуємо послідовнісь
        # та повертаємо її останній елемент за розбиттям
        plt.plot(x, y, ".b")
        return x[-1], y[-1]
    else:
        # Якщо границя послідовності відома,
        # перевіряємо, чи потрапляють останні елементи у проміжок
        s = np.abs(y - b) < eps

        k = -1
        # Якщо останній елемент послідовності не потрапив у проміжок,
        # повертаємо None
        if s[k] == 0:
            return None, None

        while s[k] > 0:
            k -= 1
        k = k % s.size + 1

        # Якщо forall=True, будуємо на графіку всі елементи,
        # інакше тільки ті, що потрапили в проміжок
        begin = 0 if forall else k

        # Будуємо графіки
        plt.plot(x[begin:], y[begin:], ".b")
        plt.plot(np.array((x[begin], x[-1])), np.array((b, b)), "-r")
        plt.plot(np.array((x[begin], x[-1])), np.array((b - eps, b - eps)), "--g")
        plt.plot(np.array((x[begin], x[-1])), np.array((b + eps, b + eps)), "--g")
        # Встановлюємо зріз ділянки, яка показує графік
        plt.axis([x[begin], x[-1], b - eps*2, b + eps*2])
        # Повертаємо номер останнього елемента послідовності,
        # який потрапив у проміжок за даним розбиттям
        return x[k], y[k]


if __name__ == "__main__":
    t = (1, 200, 1)  # параметри розбиття: (початок, кінець, крок)
    x = np.arange(*t)
    y = func01(x)
    # print(x, y)
    # print(plot_seq(x, y))
    b = 0.75  # границя
    eps = 0.01
    x0, y0 = plot_seq(x, y, b, eps, True)
    print(x0, y0)
    plt.show()
