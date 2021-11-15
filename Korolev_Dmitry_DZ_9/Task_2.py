class Road:
    def __init__(self, length, width, layer=5):
        self._width = width
        self._length = length
        self.layer = layer

    def value(self):
        return self._width * self._length * self.layer * 25


r = Road(5000, 20)
print(r.value(), 'kg')