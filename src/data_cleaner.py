from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from scipy.stats import zscore


class PreProcessor:
    def duplicate_remover(self, df: pd.DataFrame):
        return df.drop_duplicates()

    def nan_remover(self, df: pd.DataFrame):
        cols = df.columns
        numeric_cols = df.select_dtypes("number").columns

        for col in cols:
            if col in numeric_cols:
                continue

            bool_series = pd.isnull(df[col])
            df = df[~bool_series]

        return df


# Missing Value
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
        if k <= 0:
            raise ValueError("Error: Your input is invalid! Please try again.")

        numeric_cols = df.select_dtypes("number").columns

        if numeric_cols.empty:
            return df

        numeric_features = df[numeric_cols]

        imputer = KNNImputer(n_neighbors=min(k, len(df)))
        numeric_df = pd.DataFrame(
            imputer.fit_transform(numeric_features),
            columns=numeric_cols,
            index=df.index,
        )

        new_df = df.copy()
        new_df[numeric_cols] = numeric_df

        return new_df


# Outlier Values
class BaseOutlierHandler(ABC):
    @abstractmethod
    def handle(self, df: pd.DataFrame):
        pass

    def categories_df(self, df: pd.DataFrame, category):
        categories_df = df.select_dtypes(category)
        return categories_df


class IQROutlierHandler(BaseOutlierHandler):
    def handle(self, df: pd.DataFrame, factor=1.5):
        if factor <= 0:
            raise ValueError("Error: Your input is invalid! Please try again.")

        numeric_cols = self.categories_df(df, "number").columns

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
        if threshold <= 0:
            raise ValueError("Error: Your input is invalid! Please try again.")

        numeric_cols = self.categories_df(df, "number").columns

        for col in numeric_cols:
            z_score = np.abs(zscore(df[col], nan_policy="omit"))

            mask = z_score > threshold

            df.loc[mask, col] = np.nan

        return df


class Winsorization(BaseOutlierHandler):
    def handle(self, df: pd.DataFrame):
        numeric_cols = self.categories_df(df, "number").columns

        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - IQR * (1.5)
            upper_bound = Q3 + IQR * (1.5)

            df[col] = df[col].clip(lower_bound, upper_bound)

        return df
