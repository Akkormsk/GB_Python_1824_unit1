class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом', self.title)


class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой', self.title)


class Marker(Stationery):
    def draw(self):
        print('Рисуем маркером', self.title)


pencil = Pencil('Koh-i-noor')
pen = Pen('Bic')
marker = Marker('Stabilo')

pencil.draw()
pen.draw()
marker.draw()