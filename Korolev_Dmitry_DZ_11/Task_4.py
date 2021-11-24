class MyException(Exception):
    def __init__(self, text):
        if text:
            self.message = text
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return self.message
        else:
            return 'Some Error'


class Warehouse:
    def __init__(self):
        self.__stock = {}
        self.number = 0

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, val):
        if str(val).isdecimal():
            self._number = val
        else:
            print('Количество введите числом! По умолчанию принято за 0')
            self._number = 0

    def import_good(self, good, number):
        self.number = number
        good = list(globals().keys())[list(globals().values()).index(good)]
        wh_imp = list(globals().keys())[list(globals().values()).index(self)]
        good_stock = self.__stock.get(good)
        if not good_stock:
            good_stock = 0
        good_stock += self.number
        self.__stock[good] = good_stock
        print(f'На склад {wh_imp} поступило {self.number} шт {good}. Текущий остаток {good_stock} шт')

    def export_good(self, good, number):
        self.number = number
        try:
            self.__flag = 1
            good = list(globals().keys())[list(globals().values()).index(good)]
            wh_exp = list(globals().keys())[list(globals().values()).index(self)]
            good_stock = self.__stock.get(good)
            if not good_stock or good_stock < self.number:
                self.__flag = 0
                raise MyException(
                    f'Товар {good} отсутствует на складе {wh_exp} в нужном количестве. Экспорт невозможен')
            good_stock -= self.number
            self.__stock[good] = good_stock
            print(f'Со склада {wh_exp} ушло {self.number} шт {good}. Текущий остаток {good_stock} шт')
        except MyException as e:
            print(e)

    def replace_good(self, good, number, wh_imp):
        self.export_good(good, number)
        if self.__flag:
            wh_imp.import_good(good, number)

    def get_info(self):
        for i, j in globals().items():
            if j == self:
                wh = i
        print(f'\n Сводка по остаткам на складе {wh}: \n')
        summ = 0
        wei = 0
        for i, j in self.__stock.items():
            for m, n in globals().items():
                if m == i:
                    print(f'{i} - {j} шт, на общую сумму {j * n.price} руб, общий вес {j * n.weight} кг')
                    summ += j * n.price
                    wei += j * n.weight
        print(f'Сумма склада - {summ} руб, вес склада - {wei} кг \n')


class Equipment:
    def __init__(self):
        pass

    color = "white"


class Player(Equipment):
    def __init__(self):
        pass

    weight = 1.3
    price = 6000


class Scanner(Equipment):
    def __init__(self):
        pass

    weight = 1
    price = 3000


if __name__ == '__main__':
    butovo = Warehouse()
    lublino = Warehouse()
    player_01 = Player()
    scanner_01 = Scanner()
    butovo.import_good(player_01, 5)
    butovo.export_good(player_01, 3)
    butovo.export_good(player_01, 4)
    lublino.import_good(scanner_01, 9)
    lublino.replace_good(scanner_01, 3, butovo)
    butovo.replace_good(scanner_01, 5, lublino)
    butovo.get_info()
    lublino.get_info()
    butovo.import_good(player_01, 's')
