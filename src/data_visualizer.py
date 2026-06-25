import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from src.data_analyzer import DataAnalyzer


class DataVisualizer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def histogram(self, column: str):
        plt.hist(self.df[column], bins=20)
        plt.title(f"Distribution of {column.title()}")
        plt.xlabel(column.title())
        plt.ylabel("Frequency")

        plt.show()

    def box_plot(self, column: str):
        sns.boxenplot(x=self.df[column])
        plt.title(f"Distribution of {column.title()}")
        plt.show()

    def scatter(self, x_column: str, y_column: str):
        plt.title(f"{x_column.title()} Vs {y_column.title()}")

        top_genres = self.df["track_genre"].value_counts().head(10).index
        filtered_df = self.df[self.df["track_genre"].isin(top_genres)]

        colors = np.array(
            [
                "red",
                "hotpink",
                "green",
                "yellow",
                "purple",
                "cyan",
                "orange",
                "blue",
                "brown",
                "lime",
            ]
        )

        for i, genre in enumerate(filtered_df["track_genre"].unique()):
            genre_df = filtered_df[filtered_df["track_genre"] == genre]

            plt.xlabel(x_column.title())
            plt.ylabel(y_column.title())
            plt.scatter(
                genre_df[x_column], genre_df[y_column], label=genre, c=colors[i]
            )

        plt.legend()
        plt.show()

    def heatmap(self):
        da = DataAnalyzer(self.df)
        corr = da.correlation_matrix()
        sns.heatmap(corr, cmap="coolwarm", annot=True)
        plt.title("Correlation Matrix")

        plt.show()

    def top_genre(self):
        da = DataAnalyzer(self.df)
        data = da.number_tracks_of_each_genre().head(10)
        mylabels = da.number_tracks_of_each_genre().head(10).index

        plt.pie(data, labels=mylabels)
        plt.show()
