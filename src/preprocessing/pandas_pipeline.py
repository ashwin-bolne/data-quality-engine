import pandas as pd
from typing import List, Callable

def drop_high_nulls_cols(thresold: float = 0.5):
    """
    Returns a function that drops columns with null percentage above thresold
    """
    def _drop(df: pd.DataFrame) -> pd.DataFrame:
        null_pct = df.isnull().mean()

        cols_to_drop = null_pct[null_pct > thresold].index

        return df.drop(columns=cols_to_drop)

def run_pipeline(df: pd.DataFrame, steps: List[Callable[[pd.DataFrame], pd.DataFrame]]) -> pd.DataFrame:
    """
    Runs a sequence of transformation steps on the DataFrame.

    Args:
        df (pd.DataFrame): Input DataFrame
        steps (List[callable]): List of transformations functions

    Returns:
        pd.DataFrame: Transformed dataframe
    """
    for step in steps:
        df = step(df)

    return df 