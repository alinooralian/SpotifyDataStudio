import pandas as pd
from src.song import Song
from src.data_finder import resource_path
from src.data_writer import DataWriter


class DataLoader:
    def __init__(self):
        self.__dataset_path = resource_path("data/dataset.csv")
        with open(self.__dataset_path, "r", encoding="utf-8") as f:
            self.__df = pd.read_csv(f, usecols=lambda col: col != "Unnamed: 0")
            f.close()

    @property
    def df(self):
        return self.__df

    @df.setter
    def df(self, df: pd.DataFrame):
        self.__df = df


class DataReporter:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def missing_value_report(self):
        check = False
        cols = self.df.columns

        for col in cols:
            bool_series = pd.isnull(self.df[col])
            missing_rows = self.df[bool_series]

            if missing_rows.empty:
                continue

            print(f"Missing Values in {col}:\n")
            print(missing_rows)
            print("\n\n\n")

            check = True

        return check


class ObjectCreator:
    songs = []
    dw = DataWriter()

    def create_from_file(self, df: pd.DataFrame):
        ObjectCreator.songs.clear()

        for _, line in df.iterrows():
            song = Song(dict(line))
            ObjectCreator.songs.append(song)

    def append_song(self, song: Song):
        ObjectCreator.songs.append(song)
        return ObjectCreator.dw.append_line(song)
