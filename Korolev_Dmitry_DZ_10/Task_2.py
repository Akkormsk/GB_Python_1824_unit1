from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value < 40 or value > 60:
            raise ValueError('Введите размер от 40 до 60')
        self._size = value

    def consumption(self):
        return f'consumption for {self.__class__.__name__} - {round(self._size / 6.5 + 0.5, 1)} m**2'


class Suit(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, height):
        if height < 140 or height > 200:
            raise ValueError('Введите размер от 140 до 200')
        self._size = height

    def consumption(self):
        return f'consumption for {self.__class__.__name__} - {self._size * 2 / 10 + 0.3} m**2'


new_coat = Coat(55)
print(new_coat.consumption())
new_coat.size = 58
print(new_coat.consumption())

new_suit = Suit(155)
print(new_suit.consumption())
new_suit.size = 188
print(new_suit.consumption())