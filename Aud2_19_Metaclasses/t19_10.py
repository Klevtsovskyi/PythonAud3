import math


def union(classname, discname, dct):
    cls_dct = {}

    def getter(n, name=""):
        def _getter(self):
            if name and name not in dct[getattr(self, discname)]:
                raise AttributeError("Розмічене об`єднання з дискримінантом '{}' "
                                     "не має атрибута '{}'"
                                     .format(getattr(self, discname), name))
            return self[n]
        return _getter

    cls_dct[discname] = property(getter(0))
    for names in dct.values():
        for i, name in enumerate(names, 1):
            cls_dct[name] = property(getter(i, name))

    def __new__(cls, *args):
        if len(args) != len(dct[args[0]]) + 1:
            raise TypeError
        return tuple.__new__(cls, args)

    cls_dct["__new__"] = __new__

    cls = type(classname, (tuple,), cls_dct)
    return cls


def dist(p1, p2):
    if p1.coord == "polar":
        p1 = Point("cart", p1.ro * math.cos(p1.phi), p1.ro * math.sin(p1.phi))
    if p2.coord == "polar":
        p2 = Point("cart", p2.ro * math.cos(p2.phi), p2.ro * math.sin(p2.phi))
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def square(p1, p2, p3):
    a = dist(p1, p2)
    b = dist(p2, p3)
    c = dist(p3, p1)
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


if __name__ == '__main__':
    Point = union("Point", "coord", {"cart": ("x", "y"),
                                     "polar": ("ro", "phi")})
    p1 = Point("cart", 0, 0)
    p2 = Point("polar", 1, math.pi / 2)
    p3 = Point("cart", 1, 1)
    # print(p1.coord, p1.x, p1.y)
    # print(p2.coord, p2.ro, p2.phi)
    print(square(p1, p2, p3))
