def args_kwargs(f):
    def _args_kwargs(*args, **kwargs):
        if len(args) != len(kwargs):
            raise RuntimeError("Кількість позиційних параматерів не дорівню кількості ключових!")
        return f(*args, **kwargs)
    return _args_kwargs


@args_kwargs
def function(*args, **kwargs):
    s = 1
    for x, y in zip(args, kwargs.values()):
        s *= x + 1 / y
    return s


if __name__ == '__main__':
    print(function(1, 2, 3, y1=3, y2=4, y3=5))
    print(function(1, 2, y1=3))
