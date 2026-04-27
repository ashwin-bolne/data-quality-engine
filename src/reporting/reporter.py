
def print_validation_report(file_path, df, result: dict) -> None:
    """
    Print a formatted data quality report.
    """
    print("\n=== DATA QUALITY REPORT ===\n")

    print(f"File: {file_path}")
    print(f"Rows: {df.shape[0]}")
    print(f"columns: {df.shape[1]}")

    print("\n--- Schema Validation ---")

    # Missing columns
    if result["missing_columns"]:
        print(f"✘ Missing columns: {result['missing_columns']}")
    else:
        print("✔ No missing columns")

    # Unexpected columns
    if result["unexpected_columns"]:
        print(f"✘ Unexpected columns: {result['unexpected_columns']}")
    else:
        print("✔ No unexpected columns")

    # Null values
    if result["null_columns"]:
        print("✘ Null values found:")
        for col, count in result["null_columns"].items():
            print(f"   - {col}: {count}")
    else:
        print("✔ No null values")

    # Final status
    print("\n--- Final Status ---")

    if result["is_valid"]:
        print("✅ Dataset is VALID")
    else:
        print("❌ Dataset is INVALID")