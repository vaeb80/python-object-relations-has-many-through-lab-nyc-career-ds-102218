class Trip:

    _all = []

    def __init__(self, driver, passenger):
        self._driver = driver
        self._passenger = passenger
        self._all.append(self)
        # remember to keep track of all trip instances

    @classmethod
    def all(cls):
        return cls._all

    @property
    def driver(self):
        return self._driver
    @property
    def passenger(self):
        return self._passenger
