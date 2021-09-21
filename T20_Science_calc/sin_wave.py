

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig = plt.figure()
plt.axes(xlim=(0, 4), ylim=(-5, 5))
line1, line2 = plt.plot([], [], "--g", [], [], "-.r")
x = np.linspace(0, 4, 1000)


def animate(i):
    y1 = np.sin(2*np.pi*(x - 0.01 * i))
    y2 = np.cos(2*np.pi*(x + 0.01 * i))
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    return line1, line2


anim = FuncAnimation(fig, animate, frames=200, interval=20)
plt.show()
