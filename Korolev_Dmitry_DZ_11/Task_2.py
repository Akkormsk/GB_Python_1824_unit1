class ZeroDevError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    dev_1 = int(input('Введите делимое число: '))
    try:
        dev_2 = int(input('Введите делтель: '))
        if dev_2 == 0:
            raise ZeroDevError("Деление на 0 невозможно")
    except (ZeroDevError, ValueError) as e:
        print(e)
        print('Повторите ввод:')
    else:
        print('Результат: ', dev_1 / dev_2)
        break

