import pandas as pd
import os


def load_csv(path: str) -> pd.DataFrame:
    """
    Load a CSV file and return a pandas DataFrame.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("The file doesnt exist")
        if not path.lower().endswith('.csv'):
            raise AssertionError("The file fromat is not .csv")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return None
