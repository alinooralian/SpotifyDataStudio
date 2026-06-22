class Song:
    def __init__(self, info):
        self.__track_id = info["track_id"]
        self.__artists = info["artists"]
        self.__album_name = info["album_name"]
        self.__track_name = info["track_name"]
        self.__popularity = info["popularity"]
        self.__duration_ms = info["duration_ms"]
        self.__explicit = info["explicit"]
        self.__danceability = info["danceability"]
        self.__energy = info["energy"]
        self.__key = info["key"]
        self.__loudness = info["loudness"]
        self.__mode = info["mode"]
        self.__speechiness = info["speechiness"]
        self.__acousticness = info["acousticness"]
        self.__instrumentalness = info["instrumentalness"]
        self.__liveness = info["liveness"]
        self.__valence = info["valence"]
        self.__tempo = info["tempo"]
        self.__time_signature = info["time_signature"]
        self.__track_genre = info["track_genre"]

    @property
    def track_id(self):
        return self.__track_id

    @track_id.setter
    def track_id(self, value: str):
        if len(value.strip()) == 0:
            raise ValueError("You must enter at least one letter or number.")

        self.__track_id = value

    @property
    def artists(self):
        return self.__artists

    @artists.setter
    def artists(self, value: str):
        if len(value.strip()) == 0:
            raise ValueError("You must enter at least one letter or number.")

        self.__artists = value

    @property
    def album_name(self):
        return self.__album_name

    @album_name.setter
    def album_name(self, value: str):
        if len(value.strip()) == 0:
            raise ValueError("You must enter at least one letter or number.")

        self.__album_name = value

    @property
    def track_name(self):
        return self.__track_name

    @track_name.setter
    def track_name(self, value: str):
        if len(value.strip()) == 0:
            raise ValueError("You must enter at least one letter or number.")

        self.__track_name = value

    @property
    def duration_ms(self):
        return self.__duration_ms

    @duration_ms.setter
    def duration_ms(self, value: str):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a number.")

        self.__duration_ms = value

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, value: str):
        if len(value.strip()) == 0:
            raise ValueError("You must enter at least one letter or number.")

        if value != "1" and value != "0":
            raise ValueError("The input must be 0 or 1.")

        self.__mode = value

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, value: str):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a number.")

        self.__key = value

    @property
    def instrumentalness(self):
        return self.__instrumentalness

    @instrumentalness.setter
    def instrumentalness(self, value: str):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a number.")

        if value < 0 or value > 100:
            raise ValueError("Instrumentalness must be between 0 and 100")

        self.__instrumentalness = value

    @property
    def explicit(self):
        return self.__explicit

    @explicit.setter
    def explicit(self, value: str):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a boolean.(False/True)")

        if value:
            self.__explicit = "TRUE"
        else:
            self.__explicit = "FALSE"

    @property
    def tempo(self):
        return self.__tempo

    @tempo.setter
    def tempo(self, value: str):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a number.")

        self.__tempo = value

    @property
    def loudness(self):
        return self.__loudness

    @loudness.setter
    def loudness(self, value: str):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a number.")

        self.__loudness = value

    @property
    def time_signature(self):
        return self.__time_signature

    @time_signature.setter
    def time_signature(self, value: str):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a number.")

        self.__time_signature = value

    @property
    def track_genre(self):
        return self.__track_genre

    @track_genre.setter
    def track_genre(self, value: str):
        if len(value.strip()) == 0:
            raise ValueError("You must enter at least one letter or number.")

        self.__track_genre = value

    @property
    def popularity(self):
        return self.__popularity

    @popularity.setter
    def popularity(self, value):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a number.")

        if value < 0 or value > 100:
            raise ValueError("Popularity must be between 0 and 100")

        self.__popularity = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a number.")

        if value < 0 or value > 1:
            raise ValueError("Energy must be between 0 and 1")

        self.__energy = value

    @property
    def danceability(self):
        return self.__danceability

    @danceability.setter
    def danceability(self, value):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a number.")

        if value < 0 or value > 1:
            raise ValueError("Danceability must be between 0 and 1")

        self.__danceability = value

    @property
    def acousticness(self):
        return self.__acousticness

    @acousticness.setter
    def acousticness(self, value):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a number.")

        if value < 0 or value > 1:
            raise ValueError("Acousticness must be between 0 and 1")

        self.__acousticness = value

    @property
    def valence(self):
        return self.__valence

    @valence.setter
    def valence(self, value):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a number.")

        if value < 0 or value > 1:
            raise ValueError("Valence must be between 0 and 1")

        self.__valence = value

    @property
    def liveness(self):
        return self.__liveness

    @liveness.setter
    def liveness(self, value):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a number.")

        if value < 0 or value > 1:
            raise ValueError("Liveness must be between 0 and 1")

        self.__liveness = value

    @property
    def speechiness(self):
        return self.__speechiness

    @speechiness.setter
    def speechiness(self, value):
        try:
            value = eval(value)
        except:
            raise ValueError("The input must be a number.")

        if value < 0 or value > 1:
            raise ValueError("Speechiness must be between 0 and 1")

        self.__speechiness = value

    @staticmethod
    def create_from_input():
        song = Song(
            {
                "track_id": None,
                "artists": None,
                "album_name": None,
                "track_name": None,
                "popularity": None,
                "duration_ms": None,
                "explicit": None,
                "danceability": None,
                "energy": None,
                "key": None,
                "loudness": None,
                "mode": None,
                "speechiness": None,
                "acousticness": None,
                "instrumentalness": None,
                "liveness": None,
                "valence": None,
                "tempo": None,
                "time_signature": None,
                "track_genre": None,
            }
        )

        while True:
            try:
                song.track_id = input("Enter Track ID:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.artists = input("Enter Artists:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.album_name = input("Enter Album Name:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.track_name = input("Enter Track Name:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.popularity = input("Enter Popularity:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.duration_ms = input("Enter Duration_ms:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.explicit = input("Enter Explicit:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.danceability = input("Enter Danceability:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.energy = input("Enter Energy:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.key = input("Enter Key:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.loudness = input("Enter Loudness:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.mode = input("Enter Mode:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.speechiness = input("Enter Speechiness:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.acousticness = input("Enter Acousticness:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.instrumentalness = input("Enter Instrumentalness:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.liveness = input("Enter Liveness:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.valence = input("Enter Valence:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.tempo = input("Enter Tempo:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.time_signature = input("Enter Time Signature:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:
            try:
                song.track_genre = input("Enter Track Genre:\t")
                break
            except ValueError as e:
                print(f"Error: {e}")

        return song
