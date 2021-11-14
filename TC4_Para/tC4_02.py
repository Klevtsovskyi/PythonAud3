import time
import tkinter as tk
import threading


def fib(n, stop_event):
    time.sleep(0)  # Для того щоб потік не забирав усі ресурси процеса
    if stop_event.is_set():
        return 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1, stop_event) + fib(n - 2, stop_event)


class FibSubGUI:

    def __init__(self, n):
        self._top = tk.Toplevel()
        self._var = tk.StringVar(self._top, f"Fib({n}) = ...")
        self.make_widgets()

        self._stop_event = threading.Event()
        result = fib(n, self._stop_event)
        self._var.set(f"Fib({n}) = {result}")

    def make_widgets(self):
        self._top.minsize(300, 100)
        tk.Label(
            self._top,
            font=("Arial", 24),
            textvariable=self._var
        ).pack()
        tk.Button(
            self._top,
            text="Закрити",
            font=("Arial", 24),
            command=self.close
        ).pack()

    def close(self):
        self._stop_event.set()
        self._top.destroy()


class FibMainGUI:

    def __init__(self):
        self._top = tk.Tk()
        self._var = tk.IntVar(self._top, 35)
        self._make_widgets()
        self._top.mainloop()

    def _make_widgets(self):
        self._top.title("Обчислення чисел Фібоначі")
        self._top.minsize(400, 200)

        tk.Entry(
            self._top,
            font=("Arial", 24),
            textvariable=self._var
        ).pack()
        tk.Button(
            self._top,
            text="Порахувати",
            font=("Arial", 24),
            command=self._button_handler
        ).pack()
        tk.Button(
            self._top,
            text="Закрити",
            font=("Arial", 24),
            command=self._top.quit
        ).pack()

    def _button_handler(self):
        n = self._var.get()
        th = threading.Thread(target=FibSubGUI, args=(n, ), daemon=True)
        th.start()


if __name__ == '__main__':
    fmg = FibMainGUI()
