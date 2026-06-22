import src.data_cleaner as dc
from src.data_loader import DataLoader
from src.song import Song
from src.data_analyzer import DataAnalyzer
from src.data_writer import write_on_file

# CLI Dashboard
loader = DataLoader()

while True:
    print("=" * 5, "Spotify Data Studio", "=" * 5)

    print("1.Load Dataset & View Missing Vlues Report")
    print("2.Clean Missing Values")
    print("3.Handle Outliers")
    print("4.Add a New Song to the Dataset")
    print("6.Exit")
    print("=" * 30)

    choice = input("Enter Your Choice(1-5):\t")

    if choice == "1":
        if not loader.missing_value_report():
            print("There is no missing value.")
    elif choice == "2":
        loader.df = dc.nan_remover(loader.df)

        print("1.Mean\n2.Median\n3.KNN")
        print("=" * 30)

        choice = input("Enter Your Choice(1-3):\t")

        if choice == "1":
            loader.df = dc.MeanDataImputer().impute(loader.df)
        elif choice == "2":
            loader.df = dc.MedianDataImputer().impute(loader.df)
        else:
            k = int(input("Please Enter K(Recommended -> 5):\t"))
            loader.df = dc.KNNDataImputer().impute(loader.df, k)

        write_on_file(loader.df)
        loader.create_song_obj()
    elif choice == "3":
        print("1.IQR\n2.ZScore")
        print("=" * 30)

        choice = input("Enter Your Choice(1-2):\t")

        if choice == "1":
            factor = float(input("Please Enter Factor(Recommended -> 1.5)\t"))
            loader.df = dc.IQROutlierHandler().handle(loader.df, factor)
        else:
            threshold = float(input("Please Enter Threshold(Recommended -> 3)\t"))
            loader.df = dc.ZScoreOutlierHandler().handle(loader.df, threshold)

        write_on_file(loader.df)
        loader.create_song_obj()
    elif choice == "4":
        song = Song.create_from_input()
        loader.append_song(song)
    else:
        exit()