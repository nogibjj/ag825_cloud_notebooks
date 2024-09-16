from lib import read_data


def test_load_data():
    dataset = "medallists.csv"
    result_load = read_data(dataset)
    assert result_load is not None


if __name__ == "__main__":
    test_load_data()
