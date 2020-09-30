

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
a = -4*np.pi
b = 4*np.pi
m = 20
"""
a = -0.99
b = 0.99
m = 20

x = np.linspace(a, b, int((b - a) * 50))

fig = plt.figure()
ax = plt.axes(xlim=(a, b), ylim=(-4, 4))
line, = ax.plot([], [], lw=3)


def func1_sin(x, n):
    s = x.copy()
    a = x.copy()
    for k in range(2, n + 1):
        a *= -x*x / ((2*k - 2)*(2*k - 1))
        s += a
    return s


def func14(x, n):
    s = np.ones_like(x)
    a = np.ones_like(x)
    for k in range(2, n + 1):
        a *= - x * (2*k - 3) / (2*k - 2)
        s += a
    return s


def init():
    # plt.plot(x, np.sin(x), "--r")
    plt.plot(x, 1 / np.sqrt(1 + x), "--r")
    line.set_data([], [])
    return line,


def animate(i):
    y = func14(x, i + 1)
    line.set_data(x, y)
    return line,


anim = FuncAnimation(fig, animate, init_func=init, frames=m, interval=2000, repeat=True)
plt.show()
# anim.save("sin.gif", writer="pillow") # pip install pillow
