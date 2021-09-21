import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Початкові дані
a = -4*np.pi  # Початок відрізка
b = 4*np.pi   # Кінець відрізка
m = 20        # Кількість ітерацій

# Створюємо розбиття відрізка [a, b]
x = np.linspace(a, b, int((b - a) * 50))

# Зберігаємо посилання на поточне полотно,
# щоб в подальшому його використати для анімації
fig = plt.figure()
# Змінюємо масштаб осей
plt.axes(xlim=(a, b), ylim=(-5, 5))
# Створємо пустий графік і надаємо йому параметри відображення
line, = plt.plot([], [], "-b", lw=3)


def func01_sin(x, n):
    """ Повертає значення часткової суми ряду Тейлора для y = sin(x)"""
    s = x.copy()
    p = x.copy()
    for k in range(2, n + 1):
        p *= -x*x / ((2*k - 2)*(2*k - 1))
        s += p
    return s


def init():
    """ Функція, яка викликається один раз на початку анімації"""
    # Будуємо графік y = sin(x)
    plt.plot(x, np.sin(x), "--r")
    return line,


def animate(i):
    """ Функція, яка викликається при анімації
    :param i: номер ітерації
    """
    # Отримуємо масив значень часткової суми ряду Тейлора
    y = func01_sin(x, i + 1)
    # Відображаємо цей графік на полотні
    line.set_data(x, y)
    return line,


if __name__ == "__main__":
    anim = FuncAnimation(
        fig,             # Полотно, на якому буде зображено анімацію
        animate,         # Функція для анімації
        init_func=init,  # Функція, яка викликається один раз перед анімацєю
        frames=m,        # Кількість ітерацій анімації (починається з 0)
        interval=2000,   # Кількість мілісекунд на ітерацію
        repeat=True      # Чи повторювати анімацію після останньої ітерації
    )
    plt.show()
    # Збереження анімації
    # anim.save("sin.gif", writer="pillow")  # pip install pillow
