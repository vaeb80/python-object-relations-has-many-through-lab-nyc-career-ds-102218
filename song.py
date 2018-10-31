class Song:

    _all = []

    def __init__(self, name, artist, genre):
        self._name = name
        self._artist = artist
        artist._songs.append(self)
        self._genre = genre
        genre._songs.append(self)
        self._all.append(self)
        # remember to keep track of all trip instances

    @classmethod
    def all(cls):
        return cls._all
    @property
    def artist(self):
        return self._artist
    @property
    def name(self):
        return self._name
    @property
    def genre(self):
        return self._genre
