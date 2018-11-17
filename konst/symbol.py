from ._common import _verify_attr


class Symbol:
    _cache = dict()

    def __new__(cls, name):
        return cls._cache.setdefault(name, super().__new__(cls))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


def __getattr__(attr):
    _verify_attr(attr)
    return Symbol(attr)
