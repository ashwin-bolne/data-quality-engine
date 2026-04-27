from pathlib import Path 
import sys

from src.ingestion.loader import load_csv
from src.reporting.reporter import print_validation_report
from src.validation.validator import validate_schema 


def main():
    """
    Entry point for CLI execution.
    """

    # 1. Check argument provided
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_csv>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    try:
        # 2. Load data
        df = load_csv(file_path)

        # 3. Define expected schema
        expected_cols = ["id", "name", "age", "salary", "department"]

        # 4. Validate schema
        result = validate_schema(df, expected_cols)

        # 5. Print Output
        print("\n=== DATA QUALITY REPORT===")
        print(f"File: {file_path}")
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {list(df.columns)}")
        print("\nValidation Results: ")
        print_validation_report(file_path, df, result)
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()