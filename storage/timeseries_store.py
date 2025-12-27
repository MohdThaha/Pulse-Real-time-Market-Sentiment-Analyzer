from storage.database import get_connection
from utils.logger import setup_logger
from datetime import datetime

logger = setup_logger(__name__)

def init_sentiment_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sentiment_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT NOT NULL,
            source TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            confidence REAL NOT NULL,
            created_at TEXT NOT NULL,
            processed_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    logger.info("Sentiment results table ready")


def insert_sentiment(
    ticker: str,
    source: str,
    sentiment: str,
    confidence: float,
    text: str,
    created_at: str
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sentiment_results (
            ticker, source, sentiment, confidence,
            text, created_at, processed_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        ticker,
        source,
        sentiment,
        confidence,
        text,
        created_at,
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()
