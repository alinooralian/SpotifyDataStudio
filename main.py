import src.data_cleaner as dc
from src.data_loader import DataLoader
from src.song import Song
from src.data_analyzer import DataAnalyzer
from src.data_visualizer import DataVisualizer
from src.data_writer import write_on_file


def menu(options):
    while True:
        n = len(options)

        for idx, option in enumerate(options, 1):
            print(f"{idx}.{option}")

        print("=" * 30)

        choice = input(f"Enter Your Choice(1-{n}):\t")

        if int(choice) in range(1, n + 1):
            return int(choice)
        else:
            print("Error: Your Input is Invalid! Please Try again")


# CLI Dashboard
loader = DataLoader()

while True:
    print("=" * 5, "Spotify Data Studio", "=" * 5)
    choice = menu(
        [
            "Load Dataset & View Missing Vlues Report",
            "Clean Missing Values",
            "Handle Outliers",
            "Add a New Song to the Dataset",
            "Calculate Genre Insights & Correaltion Matrix",
            "Generate Advanced Visualizations",
            "Exit",
        ]
    )

    if choice == 1:
        if not loader.missing_value_report():
            print("There is no missing value.")
    elif choice == 2:
        loader.df = dc.nan_remover(loader.df)

        choice = menu(["Mean", "Median", "KNN"])

        if choice == 1:
            loader.df = dc.MeanDataImputer().impute(loader.df)
        elif choice == 2:
            loader.df = dc.MedianDataImputer().impute(loader.df)
        else:
            k = int(input("Please Enter K(Recommended -> 5):\t"))
            loader.df = dc.KNNDataImputer().impute(loader.df, k)

        write_on_file(loader.df)
        loader.create_song_obj()
    elif choice == 3:
        choice = menu(["1.IQR", "2.ZScore"])

        if choice == 1:
            factor = float(input("Please Enter Factor(Recommended -> 1.5)\t"))
            loader.df = dc.IQROutlierHandler().handle(loader.df, factor)
        else:
            threshold = float(input("Please Enter Threshold(Recommended -> 3)\t"))
            loader.df = dc.ZScoreOutlierHandler().handle(loader.df, threshold)

        write_on_file(loader.df)
        loader.create_song_obj()
    elif choice == 4:
        song = Song.create_from_input()
        loader.append_song(song)
    elif choice == 5:
        analyzer = DataAnalyzer(loader.df)

        choice = menu(["General Insights", "Genre Insights", "Correlation Matrix"])

        if choice == 1:
            choice = menu(
                [
                    "Popularity",
                    "Energy",
                    "Duration",
                    "Danceability",
                    "Tempo",
                    "Track Genre",
                    "Summary",
                ]
            )

            if choice == 1:
                methods = [
                    analyzer.most_popular_track,
                    analyzer.least_popular_track,
                    analyzer.average_popularity,
                    analyzer.most_popular_genre,
                ]
                choice = menu(
                    [
                        "Most Popular Track",
                        "Least Popular Track",
                        "Average Popularity",
                        "Most Popular Genre",
                    ]
                )

                print(methods[choice - 1]())
            elif choice == 2:
                methods = [
                    analyzer.most_energetic_track,
                    analyzer.least_energetic_track,
                    analyzer.average_energy,
                ]
                choice = menu(
                    [
                        "Most Energetic Track",
                        "Least Energetic Track",
                        "Average Energy",
                    ]
                )

                print(methods[choice - 1]())
            elif choice == 3:
                methods = [
                    analyzer.longest_track,
                    analyzer.shortest_track,
                    analyzer.average_duration,
                ]
                choice = menu(["Longest Track", "Shortest Track", "Average Duration"])

                print(methods[choice - 1]())
            elif choice == 4:
                methods = [
                    analyzer.most_danceable_track,
                    analyzer.least_danceable_track,
                ]
                choice = menu(["Most Danceable Track", "Least Danceable Track"])

                print(methods[choice - 1]())
            elif choice == 5:
                methods = [analyzer.highest_tempo_track, analyzer.lowest_tempo_track]
                choice = menu(["Highest Tempo Track", "Lowest Tempo Track"])

                print(methods[choice - 1]())
            elif choice == 6:
                methods = [
                    analyzer.most_common_genre,
                    analyzer.number_tracks_of_each_genre,
                ]
                choice = menu(["Most Common Genre", "Number of Tracks in each Genre"])

                print(methods[choice - 1]())
            else:
                summary = analyzer.summary_report()

                for key, val in summary.items():
                    print(f"{key}:\n{val}\n")
        elif choice == 2:
            genre = input(
                "Enter Your desired Genre(Input must consist of lowercase letters.):\t"
            )
            print("=" * 30)

            if analyzer.number_of_tracks_per_genre(genre) == 0:
                print(
                    "There is no information for this genre! Either change the input type or select another genre."
                )
                continue

            choice = menu(
                [
                    "Popularity",
                    "Energy",
                    "Duration",
                    "Danceability",
                    "Tempo",
                    "Track Genre",
                    "Artists",
                    "Summary",
                ]
            )

            if choice == 1:
                methods = [
                    analyzer.most_popular_track_per_genre,
                    analyzer.least_popular_track_per_genre,
                    analyzer.average_popularity_per_genre,
                ]
                choice = menu(
                    [
                        "Most Popular Track",
                        "Least Popular Track",
                        "Average Popularity",
                    ]
                )

                print(methods[choice - 1](genre))
            elif choice == 2:
                methods = [
                    analyzer.most_energetic_track_per_genre,
                    analyzer.least_energetic_track_per_genre,
                    analyzer.average_energy_per_genre,
                ]
                choice = menu(
                    [
                        "Most Energetic Track",
                        "Least Energetic Track",
                        "Average Energy",
                    ]
                )

                print(methods[choice - 1](genre))
            elif choice == 3:
                methods = [
                    analyzer.longest_track_per_genre,
                    analyzer.shortest_track_per_genre,
                    analyzer.average_duration_per_genre,
                ]
                choice = menu(["Longest Track", "Shortest Track", "Average Duration"])

                print(methods[choice - 1](genre))
            elif choice == 4:
                methods = [
                    analyzer.most_danceable_track_per_genre,
                    analyzer.least_danceable_track_per_genre,
                    analyzer.average_danceability_per_genre,
                ]
                choice = menu(
                    [
                        "Most Danceable Track",
                        "Least Danceable Track",
                        "Average Danceability",
                    ]
                )

                print(methods[choice - 1](genre))
            elif choice == 5:
                methods = [
                    analyzer.highest_tempo_track_per_genre,
                    analyzer.lowest_tempo_track_per_genre,
                    analyzer.average_tempo_per_genre,
                ]
                choice = menu(
                    ["Highest Tempo Track", "Lowest Tempo Track", "Average Tempo"]
                )

                print(methods[choice - 1](genre))
            elif choice == 6:
                methods = [analyzer.number_of_tracks_per_genre]
                choice = menu(["Number of Tracks in this Genre"])

                print(methods[choice - 1](genre))
            else:
                summary = analyzer.summary_report_per_genre(genre)

                for key, val in summary.items():
                    print(f"{key}:\n{val}\n")
        elif choice == 3:
            print(analyzer.correlation_matrix())
    elif choice == 6:
        visualizer = DataVisualizer(loader.df)

        choice = menu(["Histogram", "Box-Plot", "Scatter Plot", "Heatmap", "Pie Plot"])

        if choice == 1:
            options = [
                "Popularity",
                "Loudness",
                "Danceability",
                "Energy",
                "Speechiness",
                "Acousticness",
                "Instrumentalness",
                "Liveness",
            ]
            choice = menu(options)

            visualizer.histogram(options[choice - 1].lower())
        elif choice == 2:
            options = [
                "Popularity",
                "Loudness",
                "Danceability",
                "Energy",
                "Speechiness",
                "Acousticness",
                "Instrumentalness",
                "Liveness",
            ]
            choice = menu(options)

            visualizer.box_plot(options[choice - 1].lower())
        elif choice == 3:
            options = [
                "Popularity",
                "Loudness",
                "Danceability",
                "Energy",
                "Speechiness",
                "Acousticness",
                "Instrumentalness",
                "Liveness",
            ]
            print("X axis...")
            choice_1 = menu(options)
            print("Y axis...")
            choice_2 = menu(options)

            visualizer.scatter(options[choice_1 - 1].lower(), options[choice_2 - 1].lower())
        elif choice == 4:
            visualizer.heatmap()
        elif choice == 5:
            visualizer.top_genre()
    else:
        exit()
