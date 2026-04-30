from pathlib import Path 
import sys
import logging 

from src.ingestion.loader import load_csv
from src.reporting.reporter import print_validation_report
from src.validation.validator import validate_schema 
from src.exceptions import (InvalidFileFormatError, EmptyDatasetError, DataParsingError, SchemaMismatchError)
from src.analysis.analyzer import run_statistics
from src.analysis.scorer import quality_score
from src.preprocessing.pandas_pipeline import (
    run_pipeline,
    drop_high_null_cols,
    fill_numeric_nulls,
    encode_categoricals
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def main():
    """
    Entry point for CLI execution.
    """

    # 1. Check argument provided
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_csv> [-v] [--clean]")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    verbose = "-v" in sys.argv
    clean = "--clean" in sys.argv

    try:
        # 2. Load data
        df = load_csv(file_path)

        # 3. Define expected schema
        expected_cols = df.columns.tolist()

        # 4. Validate schema
        result = validate_schema(df, expected_cols)

        # 5. Analyze
        stats = run_statistics(df)

        # 6. Score 
        score = quality_score(df)

        # 7. Print Output
        print_validation_report(file_path, df, result)

        # 8. Print score
        print(f"\n📊 Data Quality Score: {score}")

        # 9. Verbose output
        if verbose:
            print("\n🔍 Column-wise Statistics:")
            for col, col_stats in stats.items():
                print(f"{col}: {col_stats}")

    except FileNotFoundError as e:
        logger.error(e)
        print(f"❌ File not found: {e}")
        sys.exit(1)

    except InvalidFileFormatError as e:
        logger.error(e)
        print(f"❌ Invalid file format: {e}")
        sys.exit(1)

    except EmptyDatasetError as e:
        logger.error(e)
        print(f"❌ Empty dataset: {e}")
        sys.exit(1)

    except DataParsingError as e:
        logger.error(e)
        print(f"❌ Data parsing error: {e}")
        sys.exit(1)

    except SchemaMismatchError as e:
        logger.error(e)
        print(f"❌ Schema mismatch: {e}")
        sys.exit(1)

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()