import sqlite3
import pandas as pd
import os

# ---------------------------
# Database Path
# ---------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "data", "pulse.db")


def load_sentiment_data(ticker: str) -> pd.DataFrame:
    """
    Load sentiment data for a given stock ticker
    from the Pulse SQLite database.
    """
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT created_at, sentiment, confidence
    FROM sentiment_results
    WHERE ticker = ?
    ORDER BY created_at ASC
    """

    df = pd.read_sql(query, conn, params=(ticker,))
    conn.close()

    if df.empty:
        return df

    # Normalize timestamp
    df.rename(columns={"created_at": "timestamp"}, inplace=True)

    df["timestamp"] = (
        pd.to_datetime(
            df["timestamp"],
            format="mixed",
            errors="coerce",
            utc=True
        )
        .dt.tz_convert(None)
    )

    df = df.dropna(subset=["timestamp"])

    return df


def load_recent_texts(ticker: str, limit: int = 50):
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT text
    FROM sentiment_results
    WHERE ticker = ?
      AND text IS NOT NULL
    ORDER BY created_at DESC
    LIMIT ?
    """

    df = pd.read_sql(query, conn, params=(ticker, limit))
    conn.close()

    return df["text"].tolist()
