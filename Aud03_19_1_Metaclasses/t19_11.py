

import math


class UnionTupleMeta(type):

    def __init__(cls, classname, bases, cls_dct):
        super().__init__(classname, bases, cls_dct)

        def getter(n, name=""):
            def _getter(self):
                if name and name not in cls._fields_dct[getattr(self, cls._discrname)]:
                    raise AttributeError("Розмічене об`єднання з дискримінантом '{}' "
                                         "не має атрибута '{}'"
                                         .format(getattr(self, cls._discrname), name))
                return self[n]
            return _getter

        setattr(cls, cls._discrname, property(getter(0)))
        for names in cls._fields_dct.values():
            for i, name in enumerate(names, 1):
                setattr(cls, name, property(getter(i, name)))


class UnionTuple(tuple, metaclass=UnionTupleMeta):

    _discrname = ""   # "coord"
    _fields_dct = {}  # {"cart": ("x", "y"), "polar": ("ro", "phi")}

    def __new__(cls, *args):
        if len(args) != len(cls._fields_dct[args[0]]) + 1:
            raise TypeError("Потрібно {} аргументів"
                            .format(len(cls._fields_dct[args[0]]) + 1))
        return super().__new__(cls, args)


class Point(UnionTuple):

    _discrname = "coord"
    _fields_dct = {"cart": ("x", "y"), "polar": ("ro", "phi")}


def dist(p1, p2):
    if p1.coord == "polar":
        p1 = Point("cart", p1.ro * math.cos(p1.phi), p1.ro * math.sin(p1.phi))
    if p2.coord == "polar":
        p2 = Point("cart", p2.ro * math.cos(p2.phi), p2.ro * math.sin(p2.phi))
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def square(p1, p2, p3):
    a = dist(p1, p2)
    b = dist(p2, p3)
    c = dist(p3, p1)
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


if __name__ == '__main__':
    p1 = Point("cart", 0, 0)
    p2 = Point("polar", 1, math.pi / 2)
    p3 = Point("polar", 1, 0)

    print(p1)
    print(p1.coord, p1.x, p1.y)
    print(p1[0], p1[1], p1[2])
    try:
        print(p1.ro)
    except AttributeError as e:
        print(e)

    print("Площа: ", square(p1, p2, p3))
