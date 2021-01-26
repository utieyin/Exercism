import time
import datetime


class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        n = (self.hour * 3600) + (self.minute * 60)
        t = time.strftime("%H:%M", time.gmtime(n))
        return t

    def __eq__(self, other):
        return (self.__repr__() == other.__repr__())

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)

print(Clock(-25, -160))