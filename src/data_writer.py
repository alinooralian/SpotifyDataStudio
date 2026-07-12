from src.data_finder import resource_path
from src.song import Song
import pandas as pd
import csv


class DataWriter:
    def __init__(self):
        self.__dataset_path = resource_path("data/dataset.csv")

    def write_dataset(self, df: pd.DataFrame):
        df.to_csv(self.__dataset_path, encoding="utf-8", index=False, header=True)

    def append_line(self, song: Song):
        with open(self.__dataset_path, "a", newline="", encoding="utf-8") as f:
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

        with open(self.__dataset_path, "r", encoding="utf-8") as f:
            df = pd.read_csv(f)
            f.close()
            return df
