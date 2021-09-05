

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


class TraceMeta(type):

    """def __init__(cls, classname, bases, cls_dct):
        super().__init__(classname, bases, cls_dct)
        for name, attr in cls_dct.items():
            if not name.startswith("__") and isinstance(attr, FUNCTION):
                setattr(cls, name, trace(attr))"""

    def __new__(mcs, classname, bases, cls_dct):
        for name, attr in cls_dct.items():
            if not name.startswith("__") and callable(attr):
                cls_dct[name] = trace(attr)
        return super().__new__(mcs, classname, bases, cls_dct)


class SimpleClass(metaclass=TraceMeta):

        def __init__(self):
            pass

        def f(self, x=0):
            if x:
                return self.g()

        def g(self):
            return 1


if __name__ == '__main__':
    obj = SimpleClass()
    obj.f(1)
    obj.g()
