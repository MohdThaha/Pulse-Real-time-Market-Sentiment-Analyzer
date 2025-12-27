import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    # App
    APP_NAME = os.getenv("APP_NAME", "Pulse")
    ENV = os.getenv("ENV", "development")

    # Ingestion
    DEFAULT_TICKER = os.getenv("DEFAULT_TICKER", "AAPL")
    INGESTION_INTERVAL_SECONDS = int(
        os.getenv("INGESTION_INTERVAL_SECONDS", 60)
    )

    # Twitter
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
    TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
    TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

    # Reddit
    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
    REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
    REDDIT_USER_AGENT = os.getenv(
        "REDDIT_USER_AGENT", "pulse-sentiment-analyzer"
    )

    # Database
    SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "data/pulse.db")

    # API
    SENTIMENT_API_URL = os.getenv(
        "SENTIMENT_API_URL",
        "http://127.0.0.1:8000/predict"
    )

    # Twitter via RapidAPI
    RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
    RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")




settings = Settings()
