import numpy as np
from matplotlib import pyplot as plt


NUM = 500


def taylor_sin(n):  # T20.04а
    def _taylor_sin(x):
        ak = x.copy()
        s = x.copy()
        for k in range(1, n):
            ak *= -x * x / (2 * k) / (2 * k + 1)
            s += ak
        return s

    _taylor_sin.__name__ = f"taylor(sin, {n})"
    return _taylor_sin


def lagrange(f, a, b, m):  # T20.06
    xk = np.linspace(a, b, m)
    yk = f(xk)

    def _lagrange(x):
        y = np.zeros_like(x)
        lk = np.ones_like(x)
        for k in range(m):
            lk.fill(1)
            for i in range(m):
                if i != k:
                    lk *= (x - xk[i]) / (xk[k] - xk[i])
            y += yk[k] * lk
        return y

    _lagrange.__name__ = f"lagrange({f.__name__}, {m})"
    return _lagrange


def average_error(f1, f2, xmin, xmax, ymin, ymax):
    box_square = (xmax - xmin) * (ymax - ymin)
    count = int(box_square) * NUM
    x = np.random.uniform(xmin, xmax, count)
    y = np.random.uniform(ymin, ymax, count)
    y1 = f1(x)
    y2 = f2(x)
    count_in = len(
        y[
            np.logical_or(
                np.logical_and(y1 <= y, y <= y2),
                np.logical_and(y2 <= y, y <= y1)
            )
        ]
    )
    # print(count, count_in)
    square = box_square * count_in / count
    # print(square, box_square)
    return np.sqrt(square / box_square)


def move_spines_ticks():
    a0, b0, c0, d0 = plt.axis()
    d0 = (b0 - a0) * 3 / 8
    c0 = - d0
    plt.axis([a0, b0, c0, d0])

    ax = plt.gca()
    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position(("data", 0))
    ax.spines["left"].set_position(("data", 0))
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")

    plt.legend(loc="best")


def plot_f1f2(x, f1, f2):
    y1 = f1(x)
    y2 = f2(x)

    plt.plot(x, y1, "-b", lw=2, label=f1.__name__)
    plt.plot(x, y2, "-r", lw=2, label=f2.__name__)
    plt.fill_between(x, y1, y2, facecolor="yellow")

    error = average_error(f1, f2, *plt.axis())
    print("Середня похибка наближення: ", error)

    move_spines_ticks()


def plot_diff(x, f1, f2):
    y = f2(x) - f1(x)

    plt.plot(x, y, "-m", label="difference")
    plt.fill_between(x, y, facecolor="pink")

    move_spines_ticks()


def plot_functions(a, b, n, func, *ff):
    plt.figure(figsize=(len(ff) * 6, 8))
    x = np.linspace(a, b, n)

    for i in range(len(ff)):
        plt.subplot(2, len(ff), i + 1)
        plot_f1f2(x, func, ff[i])

        plt.subplot(2, len(ff), i + 1 + len(ff))
        plot_diff(x, func, ff[i])

    plt.show()


if __name__ == "__main__":
    a = -2 * np.pi
    b = 2 * np.pi
    n = 100
    m = 6
    plot_functions(
        a, b, n,
        np.sin,
        taylor_sin(m),
        lagrange(np.sin, a, b, m)
    )
