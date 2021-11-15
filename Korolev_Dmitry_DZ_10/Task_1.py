from itertools import product


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        txt = ''
        for n in range(len(self.matrix)):
            txt += f'{self.matrix[n]}\n'
        return txt

    def __add__(self, others):
        result = Matrix([list(map(sum, zip(*i))) for i in zip(self.matrix, others.matrix)])
        return result


A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

B = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(A)
print(B)
print(A+B)
