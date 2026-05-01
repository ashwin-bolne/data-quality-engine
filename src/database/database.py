import sqlite3
from typing import Optional

DB_PATH = "quality_results.db"

def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    """
    Create and return a SQLite database connection.

    Args:
        db_path (Optional[str]): Custom database path.

    Returns:
        sqlite3.Connection: Action connection.
    """
    return sqlite3.Connection(db_path or DB_PATH)

def create_table(conn: sqlite3.Connection) -> None:
    """
    Create quality_runs table if it does nto exists.

    Args:
        conn (sqlite3.Connection): Active database connection.
    """
    query = """
    CREATE TABLE IF NOT EXISTS quality_run (
        id INTEGER PRIMARY KEY,
        filename TEXT NOT NULL,
        row_count INTEGER,
        col_count INTEGER,
        quality_score REAL,
        null_rate REAL,
        outlier_count INTEGER,
        run_at TIMESTAMP
    )
    """
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()