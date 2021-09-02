import math


def correct(a, b):
    def _correct(f):
        def __correct(*args, **kwargs):
            res = f(*args, **kwargs)
            if res < a:
                res = a
            if res > b:
                res = b
            return res
        return __correct
    return _correct


@correct(0.1, 0.5)
def c_sin(x):
    return math.sin(x)


if __name__ == '__main__':
    t = [math.pi * i / 36 for i in range(18)]
    for x in t:
        print(x, math.sin, c_sin(x))
