class Car:
    color = 'black'
    name = 'Volga'

    def __init__(self, speed: int, is_police: bool = False):
        self.speed = speed
        self.is_police = is_police
        if is_police:
            print('POLICE on the road')

    def go(self):
        print(f'{self.color} {self.name} is running')

    def stop(self):
        print(f'{self.color} {self.name} stopped')

    def turn(self, direction):
        print(f'{self.color} {self.name} turned {direction}')

    def show_speed(self):
        print(f'Current speed of {self.color} {self.name} is {self.speed}')


class TownCar(Car):
    color = 'red'
    name = 'Prius'
    topspeed = 60

    def show_speed(self):
        print(f'Current speed of {self.color} {self.name} is {self.speed}')
        if self.speed > self.topspeed:
            print(f'Slow down!')


class SportCar(Car):
    color = 'yellow'
    name = 'BMW'


class WorkCar(TownCar):
    color = 'green'
    name = 'Largus'
    topspeed = 40


class PoliceCar(Car):
    color = 'Gray'
    name = 'Priora'


my_car = TownCar(50)
my_work_car = WorkCar(70)
not_my_car = PoliceCar(100, True)

my_car.show_speed()
my_work_car.show_speed()