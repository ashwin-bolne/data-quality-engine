from pathlib import Path 
import pandas as pd
import json 
import logging
from src.exceptions import (InvalidFileFormatError, EmptyDatasetError, DataParsingError)

logger = logging.getLogger(__name__)

def load_csv(file_path: Path) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        file_path: Path to the CSV file
    
    Returns:
        DataFrame containing the data
    
    Raises:
        FileNotFoundError: If file does not exist
        InvalidFileFormatError: If file type is incorrect
        EmptyDatasetError: If file is empty
        DataParsingError: If parsing fails
    """
    logger.info(f"Loading CSV file: {file_path}")

    #1. Validate file exists
    if not file_path.exists():
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    #2. validate file extension
    if file_path.suffix.lower() != ".csv":
        logger.error(f"Invalid file type: {file_path.suffix}")
        raise InvalidFileFormatError(f"Invalid file type: {file_path.suffix}. Expected .csv")
    
    try:
        #3. Load CSV
        df = pd.read_csv(file_path)

    except pd.errors.EmptyDataError:
        logger.error("CSV file is empty")
        raise EmptyDatasetError("CSV file is empty")
    
    except pd.errors.ParserError:
        logger.error("Malformed CSV file")
        raise DataParsingError("Malformed CSV file")
    
    except Exception as e:
        logger.error(f"Unexpected error while reading CSV: {e}")
        raise DataParsingError(f"Unexpected error while reading CSV: {e}")
    
    #4. check empty dataset
    if df.empty:
        logger.error("CSV contains no data")
        raise EmptyDatasetError("CSV file is empty")
    
    logger.info("CSV loaded successfully")
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

    logger.info(f"Loading JSON file: {file_path}")

    # 1. Validate file exists
    if not file_path.exists():
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # 2. Validate extension
    if file_path.suffix.lower() != ".json":
        logger.error(f"Invalid file type: {file_path.suffix}")
        raise InvalidFileFormatError(f"Invalid file type: {file_path.suffix}. Expected .json")
    
    try:
        # 3. Read JSON file
        with file_path.open("r") as f:
            data = json.load(f)

    except json.JSONDecodeError:
        logger.error("Invalid JSON format")
        raise DataParsingError("Invalid JSON format")
    
    except Exception as e:
        logger.error(f"Unexpected error while reading JSON: {e}")
        raise DataParsingError(f"Unexpected error while reading JSON: {e}")
    
    # 4. Validate empty data 
    if not data:
        logger.error("JSON file is empty")
        raise EmptyDatasetError("JSON file is empty")
    
    try:
        # 5. Convert to DataFrame
        df = pd.DataFrame(data)

    except Exception as e:
        logger.error(f"Failed to convert JSON to DataFrame: {e}")
        raise DataParsingError(f"Failed to convert JSON to DataFrame: {e}")
    
    if df.empty:
        logger.error("JSON contains no usable data")
        raise EmptyDatasetError("JSON contains no usable data")
    
    logger.info("JSON loaded successfully")
    return df