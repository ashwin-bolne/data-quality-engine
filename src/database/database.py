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


def insert_quality_run(conn: sqlite3.Connection, result: dict) -> None:
    """
    Insert quality run record into database.
    """
    query = """
    INSERT INTO quality_runs (
        filename,
        row_count,
        col_count,
        quality_score,
        null_rate,
        outlier_count,
        run_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """

    values = (
        result["filename"],
        result["row_count"],
        result["col_count"],
        result["quality_score"],
        result["null_rate"],
        result["outlier_count"],
        result["run_at"]
    )

    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()


def get_history(conn: sqlite3.Connection, limit: int = 10):
    """
    Fetch last N runs ordered by latest timestamp.
    """
    query="""
    SELECT * 
    FROM quality_runs
    ORDER BY run_at DESC
    LIMIT ?
    """

    cursor = conn.cusor()
    cursor.execute(query, (limit, ))
    return cursor.fetchall()

def get_worst(conn: sqlite3.Connection, n: int = 5):
    """
    Fetch N worst datasets by quality_score.
    """
    query = """
    SELECT *
    FROM quality_runs
    ORDER BY quality_score ASC
    LIMIT ?
    """

    cusrsor = conn.cursor()
    cusrsor.execute(query, (n,))
    return cusrsor.fetchall()