import pandas as pd

def write_on_file(df:pd.DataFrame):
    df.to_csv("./data/dataset.csv", encoding= "utf-8", index= False, header= True)