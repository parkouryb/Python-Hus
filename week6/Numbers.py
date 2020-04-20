class Numbers:
    MULTIPLIER = 3

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    @classmethod
    def multiply(cls, a):
        return a * cls.MULTIPLIER

    @staticmethod
    def subtract(b, c):
        return b - c

    @property
    def value(self):
        return (self.x, self.y)

    @value.setter
    def value(self, xy_tuple):
        self.x, self.y = xy_tuple

    @value.deleter
    def value(self):
        del self.x
        del self.y

a = Numbers(1,2)
print(a.value)
a.value = 3,4
print(a.value)
print(a.value)
print(Numbers.subtract(1, 2))
del a.value


