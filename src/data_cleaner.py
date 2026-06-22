from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from scipy.stats import zscore

#Missing Values
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

# Outlier Values
class BaseOutlierHandler(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame):
        pass


class IQROutlierHandler(BaseOutlierHandler):
    def handle(self, df: pd.DataFrame, factor=1.5):
        numeric_cols = df.select_dtypes("number").columns

        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - IQR * factor
            upper_bound = Q3 + IQR * factor

            mask = (df[col] < lower_bound) | (df[col] > upper_bound)

            df.loc[mask, col] = np.nan

        return df


class ZScoreOutlierHandler(BaseOutlierHandler):
    def handle(self, df: pd.DataFrame, threshold=3):
        numeric_cols = df.select_dtypes("number").columns

        for col in numeric_cols:
            z_score = np.abs(zscore(df[col], nan_policy="omit"))

            mask = z_score > threshold

            df.loc[mask, col] = np.nan

        return df
