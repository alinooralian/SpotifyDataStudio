import pandas as pd
import csv
from src.song import Song

from pathlib import Path
import sys


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path
    return Path(__file__).resolve().parent.parent / relative_path


dataset_path = resource_path("data/dataset.csv")


class DataLoader:
    songs = []

    def __init__(self):
        with open(dataset_path, "r", encoding="utf-8") as f:
            self.df = pd.read_csv(f, usecols=lambda col: col != "Unnamed: 0")
            f.close()

    def missing_value_report(self):
        check = False
        cols = self.df.columns

        for col in cols:
            bool_series = pd.isnull(self.df[col])
            missing_rows = self.df[bool_series]

            if missing_rows.empty:
                continue

            print(f"Missing Vlues in {col}:\n")
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

        with open(dataset_path, "a", newline="", encoding="utf-8") as f:
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

            f.close()

        with open(dataset_path, "r", encoding="utf-8") as f:
            self.df = pd.read_csv(f, usecols=lambda col: col != "Unnamed: 0")
            f.close()
