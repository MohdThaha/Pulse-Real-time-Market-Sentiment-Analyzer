from ingestion.reddit.reddit_client import get_reddit_client

SUBREDDITS = ["stocks", "investing", "wallstreetbets"]

def fetch_reddit_posts(ticker: str, limit: int = 20):
    reddit = get_reddit_client()
    results = []

    for sub in SUBREDDITS:
        subreddit = reddit.subreddit(sub)
        for post in subreddit.new(limit=limit):
            text = f"{post.title} {post.selftext}"
            if ticker.lower() in text.lower():
                results.append({
                    "text": text,
                    "source": "reddit",
                    "created_at": post.created_utc
                })

    return results
