

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-1.5, 1.5))
line, = ax.plot([], [], lw=3)


def circle():
    x1 = np.linspace(-1, 1, 1000)
    x2 = np.linspace(1, -1, 1000)
    y1 = -np.sqrt(1 - x1*x1)
    y2 = np.sqrt(1 - x2*x2)
    return np.hstack((x1, x2)), np.hstack((y1, y2))


def reg_poly(n):
    x = np.array([np.cos(i*2*np.pi/n) for i in range(n + 1)])
    y = np.array([np.sin(i*2*np.pi/n) for i in range(n + 1)])
    return x, y


def perimeter(x, y):
    return np.sqrt((x[0] - x[1])**2 + (y[0] - y[1])**2) * (x.size - 1)


def init():
    plt.plot(*circle(), "--g")
    line.set_data([], [])
    return line,


def animate(i):
    x, y = reg_poly(2**(i+2))
    print(perimeter(x, y) / 2)
    line.set_data(x, y)
    return line,


if __name__ == '__main__':
    anim = FuncAnimation(fig, animate, init_func=init, frames=20, interval=500, repeat=True)
    plt.show()
