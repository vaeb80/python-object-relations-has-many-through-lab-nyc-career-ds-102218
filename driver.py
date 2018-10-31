# remeber to import the Trip class here
from trip import Trip
from query import Query

class Driver:

    def __init__(self, name, driving_style):
        self._name = name
        self._driving_style = driving_style

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def driving_style(self):
        return self._driving_style
    @driving_style.setter
    def driving_style(self, style):
        self._driving_style = style

    def trips(self):
        return list(filter(lambda x: x.driver == self, Trip._all))

    def passengers(self):
        self_trips = self.trips()
        return list(map(lambda x: x.passenger, self_trips))

    def trip_count(self):
        self_trips = self.trips()
        return len(self_trips)
