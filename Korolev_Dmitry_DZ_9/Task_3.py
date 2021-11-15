class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return print(self.name, self.surname)

    def get_total_income(self):
        return print(int(self._Worker__income['wage']) + int(self._Worker__income['bonus']), 'rub')


me = Position('Dmitry', 'Korolev', 'worker', 50000, 50000)
me.get_full_name()
me.get_total_income()
print(me.position)
