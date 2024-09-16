import pandas as pd


def read_data(path):
    df = pd.read_csv(path)
    return df
