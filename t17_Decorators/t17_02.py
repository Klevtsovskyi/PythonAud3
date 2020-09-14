import math


def correct(a, b):
    def _correct(f):
        def __correct(*args, **kwargs):
            res = f(*args, **kwargs)
            res = math.exp(res) + 1
            res = 1 / res
            res = (b - a) * res
            res = a + res
            return res
        return __correct
    return _correct


@correct(10, 100)
def c_sin(x):
    return math.sin(x)


if __name__ == '__main__':
    t = [math.pi * i / 36 for i in range(18)]
    for x in t:
        print(c_sin(x))
