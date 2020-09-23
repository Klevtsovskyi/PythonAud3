

class PoolMeta(type):

    def __init__(cls, classname, bases, cls_dct):
        super().__init__(classname, bases, cls_dct)
        setattr(cls, "_count", 0)
        setattr(cls, "_objects", [])

        orig_new = cls.__new__
        orig_init = cls.__init__

        def __new__(cls, *args, **kwargs):
            if cls._count < cls._max_count:
                obj = orig_new(cls)
                cls._objects.append(obj)
            else:
                obj = cls._objects[cls._count % cls._max_count]
            return obj

        def __init__(self, *args, **kwargs):
            if cls._count < cls._max_count:
                orig_init(self, *args, **kwargs)
            cls._count += 1

        setattr(cls, "__new__", __new__)
        setattr(cls, "__init__", __init__)


class SimpleClass(metaclass=PoolMeta):

    _max_count = 5

    def __init__(self, n):
        self.n = n

    def __repr__(self):  # print(obj)
        return str(self.n)


if __name__ == '__main__':
    objects = []
    for i in range(8):
        objects.append(SimpleClass(i))

    print(objects)
    print(SimpleClass._objects)
    print(SimpleClass._count)
