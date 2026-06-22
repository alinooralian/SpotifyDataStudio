import pandas as pd
import csv
from src.song import Song


class DataLoader:
    songs = []

    def __init__(self):
        with open("./data/dataset.csv", "r", encoding="utf-8") as f:
            self.df = pd.read_csv(f, usecols=lambda col: col != "Unnamed: 0")

    def missing_value_report(self):
        check = False
        cols = self.df.columns

        for col in cols:
            bool_series = pd.isnull(self.df[col])
            missing_rows = self.df[bool_series]

            if missing_rows.empty:
                continue

            print(f"Missing Vlues in {col}\n")
            print(missing_rows)
            print("\n\n\n")

            check = True

        return check

    def create_song_obj(self):
        self.songs.clear()

        for _, line in self.df.iterrows():
            song = Song(dict(line))
            self.songs.append(song)

    def append_song(self, song: Song):
        self.songs.append(song)

        with open("./data/dataset.csv", "a", encoding="utf-8") as f:
            writer = csv.writer(f)

            writer.writerow(
                [
                    song.track_id,
                    song.artists,
                    song.album_name,
                    song.track_name,
                    song.popularity,
                    song.duration_ms,
                    song.explicit,
                    song.danceability,
                    song.energy,
                    song.key,
                    song.loudness,
                    song.mode,
                    song.speechiness,
                    song.acousticness,
                    song.instrumentalness,
                    song.liveness,
                    song.valence,
                    song.tempo,
                    song.time_signature,
                    song.track_genre,
                ]
            )
