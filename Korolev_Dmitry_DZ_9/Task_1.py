from itertools import cycle
import time


class TrafficLight:
    color = ['red', 'yellow', 'green']

    def __running(self):
        print('Start')
        cyc_col = cycle(self.color)
        cyc_time = cycle([7, 2, 3])
        while True:
            print(next(cyc_col))
            time.sleep(next(cyc_time))


a = TrafficLight()
a._TrafficLight__running()
