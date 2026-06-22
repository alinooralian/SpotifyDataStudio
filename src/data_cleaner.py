from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer

class BaseImputer(ABC):
    @abstractmethod
    def impute(self, df: pd.DataFrame):
        pass


class MeanDataImputer(BaseImputer):
    def impute(self, df: pd.DataFrame):
        return df.fillna(df.mean(numeric_only=True))


class MedianDataImputer(BaseImputer):
    def impute(self, df: pd.DataFrame):
        return df.fillna(df.median(numeric_only=True))


class KNNDataImputer(BaseImputer):
    def impute(self, df: pd.DataFrame, k=5):
        imputer = KNNImputer(n_neighbors=k)

        return pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

class BaseOutlierHandler(ABC):
    @abstractmethod
    def handle():
        pass

class IQROutlierHandler(BaseOutlierHandler):
    def handle():
        pass

class ZScoreOutlierHandler(BaseOutlierHandler):
    def handle():
        pass
