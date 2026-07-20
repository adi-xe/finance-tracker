import pandas as pd


def clean_expenses(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and prepare expense data.
    """
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    df = df.dropna(subset=["date", "amount", "category"])

    df["month"] = df["date"].dt.to_period("M").astype(str)
    df["day_of_week"] = df["date"].dt.day_name()

    return df