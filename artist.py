# remeber to import the Song class here
from song import Song

class Artist:

    def __init__(self, name):
        self._name = name
        self._songs = []

    @property
    def name(self):
        return self._name

    def songs(self):
        return self._songs

    def genres(self):
        return list(map(lambda x: x.genre, self.songs()))
