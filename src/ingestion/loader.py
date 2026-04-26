from pathlib import Path 
import pandas as pd
import json 

def load_csv(file_path: Path) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        file_path: Path to the CSV file
    
    Returns:
        DataFrame containing the data
    
    Raises:
        FileNotFoundError: If file does not exist
        ValueError: if file is not CSV or is empty
        Exception: if reading fails
    """

    #1. Validate file exists
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    #2. validate file extension
    if file_path.suffix.lower() != ".csv":
        raise ValueError(f"Invalid file type: {file_path.suffix}. Expected .csv")
    
    try:
        #3. Load CSV
        df = pd.read_csv(file_path)

    except pd.errors.EmptyDataError:
        raise ValueError("CSV file is empty")
    
    except pd.errors.ParserError:
        raise RuntimeError("Malformed CSV file")
    
    except Exception as e:
        raise RuntimeError(f"Unexpected error while reading CSV: {e}")
    
    #4. check empty dataset
    if df.empty:
        raise ValueError("CSV file is empty")
    
    return df

def load_json(file_path: Path) -> pd.DataFrame:
    """
    Load a JSON file into a pandas DataFrame.

    Args:
        file_path: Path to the JSON file
    
    Returns:
        DataFrame comtaining the data

    Raises:
        FileNotFoundError: If file does not exist
        ValueError: If invalid file type of empty data
        RuntimeError: If JSON parsing fails
    """

    # 1. Validate file exists
    if not file_path.exists():
        raise FileExistsError(f"File not found {file_path}")
    
    # 2. Validate extension
    if file_path.suffix.lower() != ".json":
        raise ValueError(f"Invalid file type: {file_path.suffix}. Expected .json")
    
    try:
        # 3. Read JSON file
        with file_path.open("r") as f:
            data = json.load(f)

    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    
    except Exception as e:
        raise RuntimeError(f"Unexpected error while reading JSON: {e}")
    
    # 4. Validate empty data 
    if not data:
        raise ValueError("JSON file is empty")
    
    try:
        # 5. Convert to DataFrame
        df = pd.DataFrame(data)

    except Exception as e:
        raise RuntimeError(f"Failed to convert to JSON to DataFrame: {e}")
    
    if df.empty:
        raise ValueError("JSON contains no usable data")
    
    return df