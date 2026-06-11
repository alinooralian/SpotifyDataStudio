import csv
from song import Song


class DataLoader:
    songs = []

    def read_data_from_csv(self):
        with open("./data/dataset.csv", "r", encoding="utf-8") as f:
            lines = csv.DictReader(f)

            for line in lines:
                line.pop("")
                song = Song(line)

                self.songs.append(song)

    def append_song(self, song):
        self.songs.append(song)

        with open("./data/dataset.csv", "a", encoding="utf-8") as f:
            csv.writer.writrow(
                len(self.songs) - 1,
                song._track_id,
                song._artists,
                song._album_name,
                song._track_name,
                song._popularity,
                song._duration_ms,
                song._explicit,
                song._danceability,
                song._energy,
                song._key,
                song._loudness,
                song._mode,
                song._speechiness,
                song._acousticness,
                song._instrumentalness,
                song._liveness,
                song._valence,
                song._tempo,
                song._time_signature,
                song._track_genre,
            )
