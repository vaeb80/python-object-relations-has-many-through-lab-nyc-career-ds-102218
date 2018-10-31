# import Trip class here
from trip import Trip
from query import Query

class Passenger:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age

    def trips(self):
        return list(filter(lambda x: x.passenger == self, Trip._all))

    def drivers(self):
        self_drivers = self.trips()
        return list(map(lambda x: x.driver, self_drivers))

    def trip_count(self):
        self_trips = self.trips()
        return len(self_trips)
