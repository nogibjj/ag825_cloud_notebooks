from script import aboutdata, createplots, createsummary
import pandas as pd

path = "medallists.csv"
df = pd.read_csv(path)


def test_aboutdata():
    assert (aboutdata(df)) is not None


def test_createplots():
    assert (createplots(df)) is not None


def test_createsummary():
    assert (createsummary()) is not None


if __name__ == "__main__":
    test_aboutdata()
    test_createplots()
    test_createsummary()
