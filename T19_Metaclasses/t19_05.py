def check_types(cls):
    orig_init = cls.__init__

    def __init__(self, *args, **kwargs):
        orig_init(self, *args, **kwargs)
        for fieldname, fieldvalue in self.__dict__.items():
            if not isinstance(fieldvalue, cls._field_type[fieldname]):
                raise TypeError(f"Атрибут {fieldname} не є типом {cls._field_type[fieldname].__name__}!")

    cls.__init__ = __init__
    return cls


@check_types
class SimpleClass:

    _field_type = {"a": bool, "b": int, "c": float, "d": str}

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


if __name__ == '__main__':
    s1 = SimpleClass(True, 1, 1.1, "1")
    s2 = SimpleClass(False, 1, 1, "2")
