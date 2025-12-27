from ingestion.api_client import get_sentiment
from ingestion.twitter.search import fetch_twitter_posts
from storage.timeseries_store import insert_sentiment
from utils.logger import setup_logger
from utils.config import settings
from datetime import datetime
import time

logger = setup_logger(__name__)

# ✅ Track multiple tickers
TRACKED_TICKERS = ["AAPL", "TSLA", "NVDA", "MSFT"]


def run_ingestion():
    logger.info("Starting Pulse ingestion manager (Twitter/X search-v3)")

    for ticker in TRACKED_TICKERS:
        logger.info(f"Fetching Twitter data for ${ticker}")

        try:
            posts = fetch_twitter_posts(ticker, limit=10)
        except Exception as e:
            logger.error(f"Failed fetching tweets for {ticker}: {e}")
            continue

        for post in posts:
            text = post.get("text")
            if not text:
                continue

            sentiment = get_sentiment(text)
            if not sentiment:
                continue

            insert_sentiment(
                ticker=ticker,
                source="twitter",
                sentiment=sentiment["sentiment"],
                confidence=sentiment["confidence"],
                created_at=post.get("created_at") or datetime.utcnow().isoformat()
            )

            logger.info(
                f"Stored Twitter sentiment | "
                f"{ticker} | "
                f"{sentiment['sentiment']} "
                f"({sentiment['confidence']})"
            )

            # ⏱ Protect free API tiers
            time.sleep(1)

        # Small pause between tickers
        time.sleep(2)


if __name__ == "__main__":
    run_ingestion()
