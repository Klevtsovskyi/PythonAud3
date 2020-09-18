import math
import random


def cash(f):
    results = {}

    def _cash(*args):
        if args not in results:
            results[args] = f(*args)
        return results[args]
    return _cash


@cash
def is_prime(x):
    for i in range(2, math.floor(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def density(a, b):
    m = (b - a) * 100
    passed = 0
    for _ in range(m):
        x = random.randint(a, b)
        if is_prime(x):
            passed += 1
    return passed / m


if __name__ == '__main__':
    t = [
        (1, 50),
        (1, 100),
        (1, 200),
        (50, 100),
        (100, 200),
    ]
    for a, b in t:
        print("Щільніть простих чисел на відрізку ({}, {}): {:.0f}%"
              .format(a, b, 100 * density(a, b)))
