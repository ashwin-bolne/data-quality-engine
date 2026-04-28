from typing import Dict, Any 

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
            result[col].update({
                "mean": float(df[col].mean()),
                "std": float(df[col].std()),
                "min": float(df[col].min()),
                "max": float(df[col].max()),
            })
    return result 