import pandas as pd

def test_data():
    filename = 'data/train.csv' # or could be URL
    data = pd.read_csv(filename)

    assert data.shape[0] == 891, "data file is not 891 rows"

