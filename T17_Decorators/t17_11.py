def trace(f):
    depth = 0

    def _trace(*args, **kwargs):
        nonlocal depth
        depth += 1
        print("Входимо у функцію {}".format(f.__name__), end="; ")
        print("глибина: {}".format(depth), end="; ")
        print("позиційні параметри: {}".format(args), end="; ")
        print("ключові параметри: {}".format(kwargs))
        res = f(*args, **kwargs)
        print("Вихід з функції: {}".format(f.__name__), end="; ")
        print("глибина: {}".format(depth), end="; ")
        print("результат: {}".format(res))
        depth -= 1
        return res
    return _trace


@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


@trace
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


if __name__ == '__main__':
    print(fib(4))
    print(fact(10))
