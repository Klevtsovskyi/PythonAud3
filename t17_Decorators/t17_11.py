

def trace(f):
    depth = 0

    def _trace(*args, **kwargs):
        nonlocal depth
        depth += 1
        print("Entering function {}".format(f.__name__), end="; ")
        print("depth: {}".format(depth), end="; ")
        print("args: {}".format(args))
        print("kwargs: {}".format(kwargs), end="; ")
        res = f(*args, **kwargs)
        print("Exiting function {}".format(f.__name__), end="; ")
        print("depth: {}".format(depth), end="; ")
        print("result: {}".format(res))
        depth -= 1
        return res
    return _trace


@trace
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


@trace
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


if __name__ == '__main__':
    print(fib(10))
    print(fact(10))
