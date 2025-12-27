import requests
from utils.config import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)

BASE_URL = "https://twitter241.p.rapidapi.com/search-v3"

def search_tweets_v3(query: str, count: int = 20, search_type: str = "Latest"):
    if not settings.RAPIDAPI_KEY:
        logger.error("Missing RapidAPI key")
        return None

    headers = {
        "x-rapidapi-key": settings.RAPIDAPI_KEY,
        "x-rapidapi-host": settings.RAPIDAPI_HOST
    }

    params = {
        "query": query,
        "count": count,
        "type": search_type  # Top | Latest
    }

    try:
        response = requests.get(
            BASE_URL,
            headers=headers,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        return response.json()

    except Exception as e:
        logger.error(f"Twitter search-v3 error: {e}")
        return None
