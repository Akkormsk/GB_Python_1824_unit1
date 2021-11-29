class Road:
    def __init__(self, length, width, layer=5):
        self.__width = width
        self.__length = length
        self.layer = layer

    def value(self):
        return self.__width * self.__length * self.layer * 25


r = Road(5000, 20)
print(r.value(), 'kg')
r_1 = Road(4000, 15, 8)
print(r_1.value(), 'kg')