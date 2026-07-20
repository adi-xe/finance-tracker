import pandas as pd


def load_expenses(file_path: str) -> pd.DataFrame:
    """
    Load expense data from a CSV file.
    """
    df = pd.read_csv(file_path)
    return df