import numpy as np
import matplotlib.pyplot as plt


def func1(n):
    return (n * 3 / 2 * (1 - 1/pow(3, n+1)) * (n - 3) * pow(n, 1/n) /
            (2*n*n + 5))


def gety(f, x):
    n = x.size
    y = np.zeros(n)
    for i in range(n):
        y[i] = f(int(x[i]))
    return y


def func1_gen(n, step):
    s = 1
    p = 1
    for _ in range(n):
        p *= 1/3
        s += p
    while True:
        yield n * s * (n - 3) * pow(n, 1/n) / (2*n*n + 5)
        for _ in range(n):
            p *= 1/3
            s += p
        n += step


def func7_gen(n, step):
    s = 1
    p = 1
    for i in range(1, n):
        p *= -1
        s += (i + 1) * p
    while True:
        yield abs(s) / n
        for i in range(n, n + step):
            p *= -1
            s += (i + 1) * p
        n += step


def func11_gen(n, step):
    while True:
        yield n**20 / 2**n
        n += step


def vect(fgen, a, b, step=1):
    n = int(np.ceil((b - a) / step))
    x = np.arange(a, b, step)
    y = np.zeros(n)
    gen = fgen(a, step)
    for i in range(n):
        y[i] = next(gen)
    return x, y


def plot_seq(x, y, b=None, eps=0.01, forall=True):
    if b is None:
        plt.plot(x, y, ".b")
        return y[-1]
    else:
        k = -1
        prev = False
        for i in range(y.size):
            if abs(y[i] - b) < eps:
                if not prev:
                    k = i
                    prev = True
            else:
                prev = False

        if not prev:
            return

        begin = 0 if forall else k

        plt.plot(x[begin:], y[begin:], ".b")
        plt.plot(np.array((x[begin], x[-1])), np.array((b, b)), "-r")
        plt.plot(np.array((x[begin], x[-1])), np.array((b - eps, b - eps)), "--g")
        plt.plot(np.array((x[begin], x[-1])), np.array((b + eps, b + eps)), "--g")

        plt.xlabel("n")
        plt.ylabel("a(n)")
        plt.axis([x[begin], x[-1], b - eps*2, b + eps*2])

        return x[k]


if __name__ == '__main__':
    t = (1, 200, 1)
    #x = np.arange(*t)
    #y = gety(func1, x)
    x, y = vect(func11_gen, *t)
    #print(x, y)
    #print(plot_seq(x, y))
    b = 0
    eps = 0.001
    print(plot_seq(x, y, b, eps, False))
    plt.show()
