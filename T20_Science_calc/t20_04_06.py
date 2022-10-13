import numpy as np
from matplotlib import pyplot as plt


NUM = 500  # Множник кількість точок для методу Монте-Карло


def taylor_sin(n):  # T20.04а
    """ Повертає функцію, яка обчислює часткову суму ряду Тейлора
    для y = sin(x) до n-го елементу
    """
    def _taylor_sin(x):
        """ Повертає значення часткової суми ряду Тейлора
        для y = sin(x) до n-го елементу
        """
        ak = x.copy()
        s = x.copy()
        for k in range(1, n):
            ak *= -x * x / (2 * k) / (2 * k + 1)
            s += ak
        return s

    _taylor_sin.__name__ = f"taylor(sin, {n})"  # Надаємо назву функції
    return _taylor_sin


def lagrange(f, a, b, n):  # T20.06
    """ Повертає функцію, що обчислює значення інтерполяційного
    поліному Лагранжа, який побудовано за n точками,
    для функції f на проміжку [a, b]
    """
    xk = np.linspace(a, b, n)
    yk = f(xk)

    def _lagrange(x):
        """ Повертає значення інтерполяційного
        поліному Лагранжа, який побудовано за n точками,
        для функції f на проміжку [a, b]
        """
        y = np.zeros_like(x)
        lk = np.ones_like(x)
        for k in range(n):
            lk.fill(1)
            for i in range(n):
                if i != k:
                    lk *= (x - xk[i]) / (xk[k] - xk[i])
            y += yk[k] * lk
        return y

    _lagrange.__name__ = f"lagrange({f.__name__}, {n})"
    return _lagrange


def average_error(f1, f2, xmin, xmax, ymin, ymax):
    """ Знаходить середню похибку наближення між функції y = f1(x) та
    функції y = f2(x) в заданому прямокунику методом Монте-Карло
    :param f1: перша функція
    :param f2: друга функція
    :param xmin: ліва межа прямокутника
    :param xmax: права межа прямокутника
    :param ymin: нижня межа прямокутника
    :param ymax: верхня межа прямокутника
    """
    box_square = (xmax - xmin) * (ymax - ymin)  # Площа прямокутника
    count = int(box_square) * NUM  # Загальна кількість точок
    x = np.random.uniform(xmin, xmax, count)
    y = np.random.uniform(ymin, ymax, count)
    y1 = f1(x)
    y2 = f2(x)
    # Кількість точок, що потрапили у проміжок
    count_in = np.sum(
        np.logical_or(
            np.logical_and(y1 <= y, y <= y2),
            np.logical_and(y2 <= y, y <= y1)
        )
    )
    # print(count, count_in)
    square = box_square * count_in / count  # Площа проміжку
    # print(square, box_square)
    return np.sqrt(square / box_square)


def move_axes():
    """ Змінює масштаб осей. Переміщує осі в центр. Підписує графіки."""
    # Змінюємо масштаб осей (4 в ширину, 3 у висоту)
    a0, b0, c0, d0 = plt.axis()
    d0 = (b0 - a0) * 3 / 8
    c0 = - d0
    plt.axis([a0, b0, c0, d0])
    # Переміщуємо осі в центр
    ax = plt.gca()
    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["bottom"].set_position(("data", 0))
    ax.spines["left"].set_position(("data", 0))
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    # Підписуємо графіки
    plt.legend(loc="best")


def plot_f1f2(x, f1, f2):
    """ Будує графіки функцій y = f1(x), y = f2(x)
    та замальовує простір між ними
    :param x: розбиття
    :param f1: перша функція
    :param f2: друга функція
    """
    y1 = f1(x)
    y2 = f2(x)
    plt.plot(x, y1, "-b", lw=2, label=f1.__name__)
    plt.plot(x, y2, "-r", lw=2, label=f2.__name__)
    plt.fill_between(x, y1, y2, facecolor="yellow")

    error = average_error(f1, f2, *plt.axis())
    print(f"Середня похибка наближення для {f2.__name__}: {error}")

    move_axes()


def plot_diff(x, f1, f2):
    """ Будує графік різниці y = f2(x) - f1(x) функцій f1, f2
    та замальовує простір між віссю OX
    :param x: розбиття
    :param f1: перша функція
    :param f2: друга функція
    """
    y = f2(x) - f1(x)
    plt.plot(x, y, "-m", label="difference")
    plt.fill_between(x, y, facecolor="pink")

    move_axes()


def plot_functions(a, b, interpolated, *interpolators):
    """ Будує графік функції interpolated та всіх функцій,
    які наближають її (interpolators) на відрізку [a, b],
    а також графік їх різниці.
    На одному полотні (вікні) зображається декілька рисунків.
    :param a: ліва межа відрізку
    :param b: права межа відрізку
    :param interpolated: функція, яку наближаємо
    :param interpolators: функції, якими наближаємо
    """
    # Редагуємо розміри полотна (вікна)
    plt.figure(figsize=((b - a) / 2 * len(interpolators), 3 / 4 * (b - a)))
    x = np.linspace(a, b, int(b - a) * 50)  # Розбиття відрізку [a, b]

    for i in range(len(interpolators)):
        # Малюємо верхній рисунок
        plt.subplot(2, len(interpolators), i + 1)
        plot_f1f2(x, interpolated, interpolators[i])
        # Малюємо нижній рисунок
        plt.subplot(2, len(interpolators), i + 1 + len(interpolators))
        plot_diff(x, interpolated, interpolators[i])
    # Зображаємо графіки на екрані
    plt.show()


if __name__ == "__main__":
    a = -2 * np.pi  # Початок відрізку
    b = 2 * np.pi   # Кінець відрізку
    m = 6           # К-ть доданків в частковій сумі ряду Тейлора
    n = 6           # К-ть точок для інтерполяційного поліному Лагранжа
    plot_functions(
        a, b,
        np.sin,
        taylor_sin(m),
        lagrange(np.sin, a, b, n)
    )
