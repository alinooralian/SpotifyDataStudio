import pandas as pd


class DataAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def total_tracks(self):
        return len(self.df)

    # popularity
    def most_popular_track(self):
        return self.df.loc[self.df["popularity"].idxmax()]

    def least_popular_track(self):
        return self.df.loc[self.df["popularity"].idxmin()]

    def average_popularity(self):
        return self.df["popularity"].mean()

    def most_popular_genre(self):
        return self.df.groupby("track_genre")["popularity"].mean().idxmax()

    def most_popular_track_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks.loc[genre_tracks["popularity"].idxmax()]

    def least_popular_track_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks.loc[genre_tracks["popularity"].idxmin()]

    def average_popularity_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks["popularity"].mean()

    # energy
    def most_energetic_track(self):
        return self.df.loc[self.df["energy"].idxmax()]

    def least_energetic_track(self):
        return self.df.loc[self.df["energy"].idxmin()]

    def average_energy(self):
        return self.df["energy"].mean()

    def most_energetic_track_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks.loc[genre_tracks["energy"].idxmax()]

    def least_energetic_track_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks.loc[genre_tracks["energy"].idxmin()]

    def average_energy_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks["energy"].mean()

    # duration
    def longest_track(self):
        return self.df.loc[self.df["duration_ms"].idxmax()]

    def shortest_track(self):
        return self.df.loc[self.df["duration_ms"].idxmin()]

    def average_duration(self):
        return self.df["duration_ms"].mean()

    def longest_track_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks.loc[genre_tracks["duration_ms"].idxmax()]

    def shortest_track_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks.loc[genre_tracks["duration_ms"].idxmin()]

    def average_duration_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks["duration_ms"].mean()

    # danceability
    def most_danceable_track(self):
        return self.df.loc[self.df["danceability"].idxmax()]

    def least_danceable_track(self):
        return self.df.loc[self.df["danceability"].idxmin()]

    def most_danceable_track_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks.loc[genre_tracks["danceability"].idxmax()]

    def least_danceable_track_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks.loc[genre_tracks["danceability"].idxmin()]

    def average_danceability_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks["danceability"].mean()

    # tempo
    def highest_tempo_track(self):
        return self.df.loc[self.df["tempo"].idxmax()]

    def lowest_tempo_track(self):
        return self.df.loc[self.df["tempo"].idxmin()]

    def highest_tempo_track_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks.loc[genre_tracks["tempo"].idxmax()]

    def lowest_tempo_track_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks.loc[genre_tracks["tempo"].idxmin()]

    def average_tempo_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks["tempo"].mean()

    # track_genre
    def most_common_genre(self):
        return self.df["track_genre"].mode()[0]

    def number_tracks_of_each_genre(self):
        return self.df["track_genre"].value_counts()

    def number_of_tracks_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return len(genre_tracks)

    # artists
    def most_active_artist_of_each_genre(self):
        return self.df["artists"].value_counts()

    def most_active_artist_per_genre(self, genre):
        genre_tracks = self.df[self.df["track_genre"] == genre]

        return genre_tracks["artists"].mode()[0]

    # correlation matrix
    def correlation_matrix(self):
        return self.df.corr(numeric_only=True)

    # summary
    def summary_report(self):
        report = {
            "Total Tracks": self.total_tracks(),
            "Average Popularity": self.average_popularity(),
            "Most Popular Track": self.most_popular_track(),
            "Least Popular Track": self.least_popular_track(),
            "Most Popular Genre": self.most_popular_genre(),
            "Average Energy": self.average_energy(),
            "Most Energetic Track": self.most_energetic_track(),
            "Least Energetic Track": self.least_energetic_track(),
            "Most Danceable Track": self.most_danceable_track(),
            "Least Danceable Track": self.least_danceable_track(),
            "Longest Track": self.longest_track(),
            "Shortest Track": self.shortest_track(),
            "Average Durations": self.average_duration(),
            "Highest Tempo Track": self.highest_tempo_track(),
            "Lowest Tempo Track": self.lowest_tempo_track(),
            "Most Common Genre": self.most_common_genre(),
        }

        return report

    def summary_report_per_genre(self, genre):
        report = {
            "Total Tracks": self.number_of_tracks_per_genre(genre),
            "Average Popularity": self.average_popularity_per_genre(genre),
            "Most Popular Track": self.most_popular_track_per_genre(genre),
            "Least Popular Track": self.least_popular_track_per_genre(genre),
            "Average Energy": self.average_energy_per_genre(genre),
            "Most Energetic Track": self.most_energetic_track_per_genre(genre),
            "Least Energetic Track": self.least_energetic_track_per_genre(genre),
            "Most Danceable Track": self.most_danceable_track_per_genre(genre),
            "Least Danceable Track": self.least_danceable_track_per_genre(genre),
            "Average Danceable Track": self.average_danceability_per_genre(genre),
            "Longest Track": self.longest_track_per_genre(genre),
            "Shortest Track": self.shortest_track_per_genre(genre),
            "Average Durations": self.average_duration_per_genre(genre),
            "Highest Tempo Track": self.highest_tempo_track_per_genre(genre),
            "Lowest Tempo Track": self.lowest_tempo_track_per_genre(genre),
            "Most Active Artist": self.most_active_artist_per_genre(genre),
        }

        return report
