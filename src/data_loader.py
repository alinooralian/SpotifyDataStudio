import pandas as pd
from src.song import Song
from src.data_finder import DataFinder
from src.data_writer import DataWriter


dataset_path = DataFinder().resource_path("data/dataset.csv")


class DataLoader:
    def __init__(self):
        with open(dataset_path, "r", encoding="utf-8") as f:
            self.__df = pd.read_csv(f, usecols=lambda col: col != "Unnamed: 0")
            f.close()

    @property
    def df(self):
        return self.__df

    @df.setter
    def df(self, df: pd.DataFrame):
        self.__df = df


class Reporter:
    def missing_value_report(self, df: pd.DataFrame):
        check = False
        cols = df.columns

        for col in cols:
            bool_series = pd.isnull(df[col])
            missing_rows = df[bool_series]

            if missing_rows.empty:
                continue

            print(f"Missing Vlues in {col}:\n")
            print(missing_rows)
            print("\n\n\n")

            check = True

        return check


class ObjectCreator:
    songs = []
    dw = DataWriter()

    def create_from_file(self, df: pd.DataFrame):
        self.songs.clear()

        for _, line in df.iterrows():
            song = Song(dict(line))
            self.songs.append(song)

    def append_song(self, song: Song):
        self.songs.append(song)
        return self.dw.append_line(song)
