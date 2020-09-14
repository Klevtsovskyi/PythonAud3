import math


def positive(f):
    def _positive(*args, **kwargs):
        res = f(*args, *kwargs)
        return math.exp(res)
    return _positive


if __name__ == '__main__':
    t = [math.pi * i / 36 for i in range(18)]
    p_sin = positive(math.sin)
    for x in t:
        print(p_sin(x))
