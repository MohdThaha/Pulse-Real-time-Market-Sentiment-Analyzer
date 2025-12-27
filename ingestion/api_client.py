import requests
from utils.config import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)

def get_sentiment(text: str) -> dict:
    try:
        response = requests.post(
            settings.SENTIMENT_API_URL,
            json={"text": text},
            timeout=20
        )
        response.raise_for_status()
        return response.json()

    except Exception as e:
        logger.error(f"Sentiment API call failed: {e}")
        return None
