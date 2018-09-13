"""this is a python class which goal is learning python object"""


class MyObject():

    @classmethod
    def classmeth(cls):
        return cls

    @staticmethod
    def statemeth(arg):
        return arg

    @property
    def author(self):
        return self._author

    @property
    def email(self):
        return self._email

    def __init__(self, html):
        self._author = 'kevinten10'
        self._email = 'wshten@gmail.com'

        self.html = html

    def __len__(self):
        return len(self)

    def __getitem__(self, item):
        return 1

    def __setitem__(self, key, value):
        print('set')

    def __delitem__(self, key):
        del self._email

    def __repr__(self):
        return self.html

    def __str__(self):
        return self.html

    def __format__(self, format_spec):
        return format_spec

    def __bytes__(self):
        return bytes

    def __abs__(self):
        return 1

    def __bool__(self):
        return 1

    def __hash__(self):
        return hash(self)

    def __eq__(self, other):
        return hash(self) == hash(other)
