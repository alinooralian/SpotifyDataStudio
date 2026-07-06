import src.data_cleaner as dc
import src.data_loader as dl
import src.data_writer as dw
from src.song import Song
from src.data_analyzer import DataAnalyzer
import src.data_visualizer as dv
from time import sleep
import os


def clean(t=0):
    sleep(t)
    os.system("cls" if os.name == "nt" else "clear")


def menu(options):
    while True:
        n = len(options)

        for idx, option in enumerate(options, 1):
            print(f"{idx}.{option}")

        print("=" * 30)

        choice = input(f"Enter Your Choice(1-{n}):\t")

        try:
            if int(choice) in range(1, n + 1):
                clean()
                return int(choice)
            else:
                print("Error: Your Input is Invalid! Please Try again")
                clean(2)
        except:
            print("Error: Your Input is Invalid! Please Try again")
            clean(2)


# CLI Dashboard
loader = dl.DataLoader()
reporter = dl.Reporter()
object_manager = dl.ObjectCreator()
writer = dw.DataWriter()

while True:
    clean()

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
        if not reporter.missing_value_report(loader.df):
            print("There is no missing value.")
            clean(2)
        else:
            input("\n\n\nPress ENTER to return...")
    elif choice == 2:
        loader.df = dc.PreProcessor().nan_remover(loader.df)
        loader.df = dc.PreProcessor().duplicate_remover(loader.df)

        choice = menu(["Mean", "Median", "KNN"])

        if choice == 1:
            loader.df = dc.MeanDataImputer().impute(loader.df)
        elif choice == 2:
            loader.df = dc.MedianDataImputer().impute(loader.df)
        else:
            while True:
                try:
                    k = int(input("Please Enter K(Recommended -> 5):\t"))
                    break
                except:
                    print("Error: Your input is invalid! Please try again.")

            loader.df = dc.KNNDataImputer().impute(loader.df, k)

        writer.write_dataset(loader.df)
        object_manager.create_from_file(loader.df)

        clean()
    elif choice == 3:
        choice = menu(["IQR", "ZScore", "Winsorization"])

        if choice == 1:
            while True:
                try:
                    factor = float(input("Please Enter Factor(Recommended -> 1.5):\t"))
                    break
                except:
                    print("Error: Your input is invalid! Please try again.")

            loader.df = dc.IQROutlierHandler().handle(loader.df, factor)
        elif choice == 2:
            while True:
                try:
                    threshold = float(
                        input("Please Enter Threshold(Recommended -> 3):\t")
                    )
                    break
                except:
                    print("Error: Your input is invalid! Please try again.")

            loader.df = dc.ZScoreOutlierHandler().handle(loader.df, threshold)
        else:
            loader.df = dc.Winsorization().handle(loader.df)

        writer.write_dataset(loader.df)
        object_manager.create_from_file(loader.df)

        clean()
    elif choice == 4:
        song = Song.create_from_input()
        loader.df = object_manager.append_song(song)

        clean()
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
                input("\n\n\nPress ENTER to return...")
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
                input("\n\n\nPress ENTER to return...")
            elif choice == 3:
                methods = [
                    analyzer.longest_track,
                    analyzer.shortest_track,
                    analyzer.average_duration,
                ]
                choice = menu(["Longest Track", "Shortest Track", "Average Duration"])

                print(methods[choice - 1]())
                input("\n\n\nPress ENTER to return...")
            elif choice == 4:
                methods = [
                    analyzer.most_danceable_track,
                    analyzer.least_danceable_track,
                ]
                choice = menu(["Most Danceable Track", "Least Danceable Track"])

                print(methods[choice - 1]())
                input("\n\n\nPress ENTER to return...")
            elif choice == 5:
                methods = [analyzer.highest_tempo_track, analyzer.lowest_tempo_track]
                choice = menu(["Highest Tempo Track", "Lowest Tempo Track"])

                print(methods[choice - 1]())
                input("\n\n\nPress ENTER to return...")
            elif choice == 6:
                methods = [
                    analyzer.most_common_genre,
                    analyzer.number_tracks_of_each_genre,
                ]
                choice = menu(["Most Common Genre", "Number of Tracks in each Genre"])

                print(methods[choice - 1]())
                input("\n\n\nPress ENTER to return...")
            else:
                summary = analyzer.summary_report()

                for key, val in summary.items():
                    print(f"{key}:\n{val}\n")

                input("\n\n\nPress ENTER to return...")
        elif choice == 2:
            genre = input(
                "Enter Your desired Genre:\t"
            ).lower()

            print("=" * 30)

            if analyzer.number_of_tracks_per_genre(genre) == 0:
                print(
                    "There is no information for this genre! Either change the input type or select another genre."
                )
                clean(2)
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
                input("\n\n\nPress ENTER to return...")
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
                input("\n\n\nPress ENTER to return...")
            elif choice == 3:
                methods = [
                    analyzer.longest_track_per_genre,
                    analyzer.shortest_track_per_genre,
                    analyzer.average_duration_per_genre,
                ]
                choice = menu(["Longest Track", "Shortest Track", "Average Duration"])

                print(methods[choice - 1](genre))
                input("\n\n\nPress ENTER to return...")
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
                input("\n\n\nPress ENTER to return...")
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
                input("\n\n\nPress ENTER to return...")
            elif choice == 6:
                methods = [analyzer.number_of_tracks_per_genre]
                choice = menu(["Number of Tracks in this Genre"])

                print(methods[choice - 1](genre))
                input("\n\n\nPress ENTER to return...")
            else:
                summary = analyzer.summary_report_per_genre(genre)

                for key, val in summary.items():
                    print(f"{key}:\n{val}\n")

                input("\n\n\nPress ENTER to return...")
        elif choice == 3:
            print(analyzer.correlation_matrix())
            input("\n\n\nPress ENTER to return...")
    elif choice == 6:
        choice = menu(
            ["Histogram", "Box-Plot", "Scatter Plot", "Heatmap", "Top Genres"]
        )

        if choice == 1:
            histogram = dv.HistogramPlotter(loader.df)

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

            histogram.create_plot(options[choice - 1].lower())
        elif choice == 2:
            box_plot = dv.BoxPlotter(loader.df)

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

            box_plot.create_plot(options[choice - 1].lower())
        elif choice == 3:
            scatter = dv.ScatterPlotter(loader.df)

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

            scatter.create_plot(
                options[choice_1 - 1].lower(), options[choice_2 - 1].lower()
            )
        elif choice == 4:
            heatmap = dv.HeatmapPlotter(loader.df)
            heatmap.create_plot()
        elif choice == 5:
            choice = menu(["Pie Chart", "Bar Plot"])

            if choice == 1:
                pie_chart = dv.PiechartPlotter(loader.df)
                pie_chart.create_plot()
            elif choice == 2:
                bar_plot = dv.BarPlotter(loader.df)
                bar_plot.create_plot()
    else:
        exit()
