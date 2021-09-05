

def only_args(f):
    def _only_args(*args, **kwargs):
        if kwargs:
            raise RuntimeError("Функції передано ключові параметри")
        return f(*args, **kwargs)
    return _only_args


@only_args
def function(*args, **kwargs):
    if max(args) > sum(args):
        return 1
    s = 0
    for x in args:
        if x > 0:
            s += x
    return s


if __name__ == '__main__':
    print(function(2, -1, 0, 3, 4, -3))
    print(function(3, 4, x3=3))
