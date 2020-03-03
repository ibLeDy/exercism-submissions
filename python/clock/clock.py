class Clock:
    def __init__(self, hour, minute):
        over_hour = minute // 60
        self.minute = minute % 60
        self.hour = (hour + over_hour) % 24

    def __repr__(self):
        return "{:02d}:{:02d}".format(self.hour, self.minute)

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        over_hour = (self.minute + minutes) // 60
        self.minute = (self.minute + minutes) % 60
        self.hour = (self.hour + over_hour) % 24
        return self

    def __sub__(self, minutes):
        over_hour = (self.minute - minutes) // 60
        self.minute = (self.minute - minutes) % 60
        self.hour = (self.hour + over_hour) % 24
        return self
