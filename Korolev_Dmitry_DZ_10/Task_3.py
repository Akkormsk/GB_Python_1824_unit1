class Cell:
    def __init__(self, num):
        self.num = num

    def __setattr__(self, attr, value):
        if attr == "num":
            self.__dict__[attr] = value
        else:
            print(f"Атрибут {attr} недопустим")

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __floordiv__(self, other):
        return self.num // other.num

    def make_order(self, row_num):
        string = ''
        i = 0
        cell_num = self.num
        while cell_num:
            string += '*'
            i += 1
            cell_num -= 1
            if i == row_num:
                string += '\n'
                i = 0
        return string


A = Cell(9)
B = Cell(2)

C = Cell(0)
D = Cell(0)
E = Cell(0)
F = Cell(0)

C.num = A + B
D.num = A - B
E.num = A * B
F.num = A // B
print(A, B, C, D, E, F)
print(A.make_order(4))
print(E.make_order(5))
