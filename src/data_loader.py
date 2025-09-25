
import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, parse_dates=["Date"])
    df["Month"] = df["Date"].dt.to_period("M")
    return df
