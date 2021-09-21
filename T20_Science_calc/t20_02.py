import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def circle():
    """ Повертає масиви numpy для зображення одиничного кола"""
    x1 = np.linspace(-1, 1, 1000)
    x2 = np.linspace(1, -1, 1000)
    y1 = -np.sqrt(1 - x1*x1)
    y2 = np.sqrt(1 - x2*x2)
    return np.hstack((x1, x2)), np.hstack((y1, y2))


def reg_poly(n):
    """ Повертає масиви numpy для зображення правильного n-кутника"""
    x = np.array([np.cos(i*2*np.pi/n) for i in range(n + 1)])
    y = np.array([np.sin(i*2*np.pi/n) for i in range(n + 1)])
    return x, y


def perimeter(x, y):
    """ Повертає периметр правильного n-кутника за його масивами numpy"""
    return np.sqrt((x[0] - x[1])**2 + (y[0] - y[1])**2) * (x.size - 1)


# Зберігаємо посилання на поточне полотно,
# щоб в подальшому його використати для анімації
fig = plt.figure()
# Змінюємо масштаб осей
plt.axes(xlim=(-2, 2), ylim=(-1.5, 1.5))
# Зображуємо одиничне коло, червоним пунктиром та товщиною 6
plt.plot(*circle(), "--r", lw=6)
# Створємо пустий графік і надаємо йому параметри відображення
line, = plt.plot([], [], "-b", lw=3)


def animate(i):
    """ Функція, яка викликається при анімації
    :param i: номер ітерації
    """
    # Отримуємо координати n-кутника
    x, y = reg_poly(2**(i + 2))
    # Шукаємо та виводимо на екран його периметр
    print(perimeter(x, y) / 2)
    # Відображаємо його на полотні
    line.set_data(x, y)
    return line,


if __name__ == "__main__":
    anim = FuncAnimation(
        fig,           # Полотно, на якому буде зображено анімацію
        animate,       # Функція для анімації
        frames=15,     # Кількість ітерацій анімації (починається з 0)
        interval=500,  # Кількість мілісекунд на ітерацію
        repeat=True    # Чи повторювати анімацію після останньої ітерації
    )
    plt.show()
