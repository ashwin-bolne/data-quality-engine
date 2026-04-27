import pandas as pd
from typing import Dict, List

from src.exceptions import SchemaMismatchError

def validate_schema(df: pd.DataFrame, expected_cols: List[str]) -> Dict:
    """
    Validate schema of a DataFrame.

    Args:
        df: Input DataFrame
        expected_cols: List of expected column names

    Returns:
        Dictionary containing schema validation results
    """
    actual_cols = list(df.columns)

    # 1. Missing columns
    misssing_columns = [col for col in expected_cols if col not in actual_cols]

    # 2. Unexpected columns
    unexpected_columns = [col for col in actual_cols if col not in expected_cols]

    #3. Null value counts 
    null_columns = {
        col: int(df[col].isnull().sum())
        for col in actual_cols
        if df[col].isnull().sum() > 0
    }

    # 4. Final Validity 
    is_valid = len(misssing_columns) == 0

    # raise error is schema is invalid
    if not is_valid:
        raise SchemaMismatchError(f"Schema mismatch | Missing: {misssing_columns} | Unexpected: {unexpected_columns}")

    return {
        "missing_columns": misssing_columns,
        "unexpected_columns": unexpected_columns,
        "null_columns": null_columns,
        "is_valid": is_valid,
    }