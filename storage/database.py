import sqlite3
from utils.config import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)

def get_connection():
    try:
        conn = sqlite3.connect(
            settings.SQLITE_DB_PATH,
            check_same_thread=False
        )
        return conn
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise
