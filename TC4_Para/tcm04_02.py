

import tkinter as tk
from concurrent.futures import ThreadPoolExecutor


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


class FibSubGUI:

    def __init__(self, n):
        self._top = tk.Toplevel()
        self._top.minsize(300, 100)

        lbl = tk.Label(self._top,
                       text="Fib({})=...".format(n),
                       font=("Arial", 24))
        lbl.pack()
        btn = tk.Button(self._top,
                        text="Закрити",
                        font=("Arial", 24),
                        command=self._top.destroy)
        btn.pack()

        result = fib(n)
        lbl.configure(text="Fib({})={}".format(n, result))


class FibMainGUI:

    def __init__(self):
        self._top = tk.Tk()
        self._executor = ThreadPoolExecutor(max_workers=2)

        self._var = tk.IntVar(self._top, 10)
        self._make_widgets()
        self._top.mainloop()

    def _make_widgets(self):
        self._top.title("Обчислення чисел Фібоначі")
        self._top.minsize(400, 200)

        ent = tk.Entry(self._top,
                       font=("Arial", 24),
                       textvariable=self._var)
        ent.pack()
        btn = tk.Button(self._top,
                        text="Порахувати",
                        font=("Arial", 24),
                        command=self._button_handler)
        btn.pack()
        btn = tk.Button(self._top,
                        text="Закрити",
                        font=("Arial", 24),
                        command=self._top.quit)
        btn.pack()

    def _button_handler(self):
        n = self._var.get()
        self._executor.submit(FibSubGUI, n)


if __name__ == '__main__':
    FibMainGUI()
