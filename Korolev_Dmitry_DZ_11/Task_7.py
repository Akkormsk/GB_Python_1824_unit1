from numbers import Number

class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    @property
    def re(self):
        return self._re

    @re.setter
    def re(self, val):
        if isinstance(val, Number):
            self._re = val
        else:
            print('Повторите ввод числа')
            self._re = 0

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return Complex((self.re * other.re) - (self.im * other.im), (self.im * other.re) + (self.re * other.im))

    def __truediv__(self, other):
        a = self.re
        b = self.im
        c = other.re
        d = other.im
        return Complex((a*c + b*d)/(c**2 + d**2),(b*c - a*d)/(c**2 + d**2))

    def __str__(self):
        return f'{self.re}+{self.im}j' if self.im > 0 else f'{self.re}{self.im}j'


a = Complex(3, 4)
b = Complex(4, -5)
print(a + b)
print(a * b)
print(a / b)

# c = 3 + 4j
# d = 4 - 5j
# # print(c/d)

c = Complex('a', 3)
print(a + c)
