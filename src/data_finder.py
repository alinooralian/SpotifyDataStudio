from pathlib import Path
import sys


class DataFinder:
    def resource_path(self, relative_path):
        if hasattr(sys, "_MEIPASS"):
            return Path(sys._MEIPASS) / relative_path
        return Path(__file__).resolve().parent.parent / relative_path
