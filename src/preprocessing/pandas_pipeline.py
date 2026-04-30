import pandas as pd
from typing import List, Callable

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