# data_collection/collect_data.py

import pandas as pd

def load_data():
    """
    Loads the election dataset from the specified GitHub raw URL.

    Returns:
        pd.DataFrame: The loaded dataset as a pandas DataFrame.
    """
    url = "https://raw.githubusercontent.com/sandeep-reddy-01/datasets/main/feb_2025_elections_dataset.csv"
    df = pd.read_csv(url)
    return df
