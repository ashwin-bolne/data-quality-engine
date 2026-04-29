from typing import Dict, Any 
import numpy as np

import pandas as pd 

def detect_nulls(df: pd.DataFrame) -> Dict[str, float]:
    """
    Calculate the percentage of null values for each column.

    Args:
        df (pd.DataFrame): Input dataset

    Returns:
        Dict[str, float]: Mapping of column name to null percentage (0.0-1.0)
    """
    return {col: float(df[col].isnull().mean()) for col in df.columns}

def run_statistics(df: pd.DataFrame) -> Dict[str, Dict[str, Any]]:
    """
    Compute stastics for dataset columns.

    for numeric columns:
        - mean, std, min, max, null_pct

    for non-numeric columns:
        - null_pct only

    Args:
        df (pd.DataFrame): Input dataset.
    
    Returns:
        Dict[str, Dict[str, Any]] = Column-wise stastics.
    """
    result: Dict[str, Dict[str, Any]] = {}

    null_percentages = detect_nulls(df)

    numeric_cols = df.select_dtypes(include="number").columns

    for col in df.columns:
        result[col] = {
            "null_pct": null_percentages[col]
        }

        if col in numeric_cols:
            arr = df[col].to_numpy()

            result[col].update({
                "mean": float(np.nanmean(arr)),
                "std": float(np.nanstd(arr)),
                "min": float(np.nanmin(arr)),
                "max": float(np.nanmax(arr)),
                "p25": float(np.nanpercentile(arr, 25)),
                "p75": float(np.nanpercentile(arr, 75)),
            })
    return result 


if __name__ == "__main__":
    import pandas as pd
    import numpy as np

    df = pd.DataFrame({
        "A": [1, 2, np.nan, 4],
        "B": [10, 20, 30, 40],
        "C": ["x", "y", "z", None]
    })

    print(run_statistics(df))