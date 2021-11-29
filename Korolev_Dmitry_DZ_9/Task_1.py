from itertools import cycle
import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        print('Start')
        cyc_col = cycle(self.__color)
        cyc_time = cycle([7, 2, 3])
        while True:
            print(next(cyc_col))
            time.sleep(next(cyc_time))


a = TrafficLight()
a.running()

