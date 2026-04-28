from typing import Dict 

import pandas as pd 

ROW_COUNT_THRESHOLD = 100

def _compute_null_score(df: pd.DataFrame) -> float:
    """
    Compute score based on overall null percentage.
    
    Args:
        df (pd.DataFrame): Input dataset.

    Returns:
        float: Null score between 0.0 and 0.1.
    """
    total_cells = df.size
    null_cells = df.isnull().sum().sum()

    if total_cells == 0:
        return 0.0
    
    null_pct = null_cells / total_cells
    return 1.0 - null_pct

def _compute_dtype_score(df: pd.DataFrame) -> float:
    """
    Compute score based on proportion of numeric columns.

    Args:
        df (pd.DataFrame): Input Dataset.

    Returns:
        float: Dtype score between 0.0 and 1.0.
    """
    total_columns = len(df.columns)

    if total_columns == 0:
        return 0.0

    numeric_columns = len(df.select_dtypes(include="number").columns)
    return numeric_columns / total_columns

def _compute_row_score(df: pd.DataFrame) -> float:
    """
    Compute score based on dataset size. 
    
    Args:
        df (pd.DataFrame): Input dataset.

    Returns:
        float: Row count score between 0.0 and 1.0.    
    """
    row_count = len(df)

    return min(row_count / ROW_COUNT_THRESHOLD, 1.0)

def quality_score(df: pd.DataFrame) -> float:
    """
    Compute overall data quality score.

    combines:
    - null score (50%)
    - dtype score (30%)
    - row count score (20%)

    Args:
        df (pd.DataFrame): Input dataset.

    Returns:
        float: Final quality score between 0.0 and 1.0.
    """
    null_score = _compute_null_score(df)
    dtype_score = _compute_dtype_score(df)
    row_score = _compute_row_score(df)

    score = (
        0.5 * null_score +
        0.3 * dtype_score +
        0.2 * row_score
    )

    return round(score, 4)