from ingestion.twitter.twitter_client import search_tweets_v3
from datetime import datetime

def fetch_twitter_posts(ticker: str, limit: int = 20):
    query = ticker  # Example: AAPL

    raw = search_tweets_v3(query=query, count=limit)
    if not raw:
        return []

    tweets = []

    instructions = (
        raw.get("result", {})
           .get("timeline_response", {})
           .get("timeline", {})
           .get("instructions", [])
    )

    for instr in instructions:
        if instr.get("__typename") != "TimelineAddEntries":
            continue

        for entry in instr.get("entries", []):
            content = entry.get("content", {})
            item = content.get("content", {}) or content
            tweet_results = item.get("tweet_results", {})
            result = tweet_results.get("result", {})

            # Handle TweetWithVisibilityResults
            if "tweet" in result:
                result = result.get("tweet", {})

            details = result.get("details")
            if not details:
                continue

            text = details.get("full_text")
            created_at_ms = details.get("created_at_ms")

            if not text:
                continue

            created_at = (
                datetime.utcfromtimestamp(created_at_ms / 1000)
                if created_at_ms else None
            )

            tweets.append({
                "text": text,
                "source": "twitter",
                "created_at": created_at
            })

            if len(tweets) >= limit:
                return tweets

    return tweets
