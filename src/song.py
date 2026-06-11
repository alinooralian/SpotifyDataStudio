class Song:
    def __init__(self, info):
        self._track_id = info["track_id"]
        self._artists = info["artists"]
        self._album_name = info["album_name"]
        self._track_name = info["track_name"]
        self._popularity = info["popularity"]
        self._duration_ms = info["duration_ms"]
        self._explicit = info["explicit"]
        self._danceability = info["danceability"]
        self._energy = info["energy"]
        self._key = info["key"]
        self._loudness = info["loudness"]
        self._mode = info["mode"]
        self._speechiness = info["speechiness"]
        self._acousticness = info["acousticness"]
        self._instrumentalness = info["instrumentalness"]
        self._liveness = info["liveness"]
        self._valence = info["valence"]
        self._tempo = info["tempo"]
        self._time_signature = info["time_signature"]
        self._track_genre = info["track_genre"]

    @property
    def popularity(self):
        return self._popularity

    @popularity.setter
    def popularity(self, value):
        if value < 0 or value > 100:
            raise ValueError("Popularity must be between 0 and 100")

        self._popularity = value

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        if value < 0 or value > 1:
            raise ValueError("Energy must be between 0 and 1")

        self._energy = value

    @property
    def danceability(self):
        return self._danceability

    @danceability.setter
    def danceability(self, value):
        if value < 0 or value > 1:
            raise ValueError("Danceability must be between 0 and 1")

        self._danceability = value

    @property
    def acousticness(self):
        return self._acousticness

    @acousticness.setter
    def acousticness(self, value):
        if value < 0 or value > 1:
            raise ValueError("Acousticness must be between 0 and 1")

        self._acousticness = value

    @property
    def valence(self):
        return self._valence

    @valence.setter
    def valence(self, value):
        if value < 0 or value > 1:
            raise ValueError("Valence must be between 0 and 1")

        self._valence = value

    @property
    def liveness(self):
        return self._liveness

    @liveness.setter
    def liveness(self, value):
        if value < 0 or value > 1:
            raise ValueError("Liveness must be between 0 and 1")

        self._liveness = value

    @property
    def speechiness(self):
        return self._speechiness

    @speechiness.setter
    def speechiness(self, value):
        if value < 0 or value > 1:
            raise ValueError("Speechiness must be between 0 and 1")

        self._speechiness = value
