import pandas as pd
from pathlib import Path
import sys


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS) / relative_path
    return Path(__file__).resolve().parent.parent / relative_path


def write_on_file(df: pd.DataFrame):
    dataset_path = resource_path("data/dataset.csv")
    df.to_csv(dataset_path, encoding="utf-8", index=False, header=True)
