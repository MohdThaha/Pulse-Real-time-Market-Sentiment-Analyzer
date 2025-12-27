import sys
import os

# ---------------------------
# Fix import paths
# ---------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from streamlit_autorefresh import st_autorefresh

from dashboard.utils import load_sentiment_data, load_recent_texts
from models.topic.keybert_model import TopicExtractor


# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Pulse — Market Sentiment",
    layout="wide"
)

# ---------------------------
# Auto Refresh (30 sec)
# ---------------------------
st_autorefresh(interval=30_000, key="pulse_refresh")

st.title("📈 Pulse — Real-time Market Sentiment Analyzer")

# ---------------------------
# Sidebar Controls
# ---------------------------
st.sidebar.header("Controls")

ticker = st.sidebar.selectbox(
    "Select Stock Ticker",
    ["AAPL", "TSLA", "NVDA", "MSFT"]
)

# ---------------------------
# Load Data
# ---------------------------
df = load_sentiment_data(ticker)

if df.empty:
    st.warning("No sentiment data available yet.")
    st.stop()

# ---------------------------
# Sentiment Mapping
# ---------------------------
sentiment_map = {
    "negative": -1,
    "neutral": 0,
    "positive": 1
}

df["sentiment_score"] = df["sentiment"].map(sentiment_map)

# ---------------------------
# Rolling Sentiment (15 min)
# ---------------------------
df = df.sort_values("timestamp")

df["rolling_sentiment"] = (
    df.set_index("timestamp")["sentiment_score"]
      .rolling("15min")
      .mean()
      .values
)

# ---------------------------
# 🚨 Market Alert
# ---------------------------
st.subheader("🚨 Market Sentiment Alert")

latest_sentiment = df["rolling_sentiment"].iloc[-1]

if latest_sentiment < -0.6:
    st.error("🚨 Sharp NEGATIVE sentiment spike detected! Possible breaking news.")
elif latest_sentiment > 0.6:
    st.success("📈 Strong POSITIVE sentiment momentum detected.")
else:
    st.info("ℹ️ Sentiment is stable.")

# ---------------------------
# Layout
# ---------------------------
col1, col2 = st.columns(2)

# 📊 Sentiment Over Time
with col1:
    st.subheader("Sentiment Over Time")

    fig, ax = plt.subplots()

    ax.plot(df["timestamp"], df["sentiment_score"], alpha=0.3, label="Raw")
    ax.plot(df["timestamp"], df["rolling_sentiment"], linewidth=2, label="15-min Avg")

    ax.set_ylabel("Sentiment")
    ax.set_xlabel("Time")
    ax.set_yticks([-1, 0, 1])
    ax.set_yticklabels(["Negative", "Neutral", "Positive"])

    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(
        mdates.ConciseDateFormatter(ax.xaxis.get_major_locator())
    )

    plt.xticks(rotation=45)
    ax.legend()
    fig.tight_layout()
    st.pyplot(fig)

# 📦 Sentiment Distribution
with col2:
    st.subheader("Sentiment Distribution")

    sentiment_counts = df["sentiment"].value_counts()

    fig2, ax2 = plt.subplots()
    sentiment_counts.plot(kind="bar", ax=ax2)
    ax2.set_ylabel("Count")

    st.pyplot(fig2)

# ---------------------------
# 📦 Tweet Volume
# ---------------------------
st.subheader("Tweet Volume Over Time (5-min window)")

volume_df = (
    df.set_index("timestamp")
      .resample("5min")
      .count()
)

fig3, ax3 = plt.subplots()
ax3.plot(volume_df.index, volume_df["sentiment"])
ax3.set_ylabel("Tweet Count")
ax3.set_xlabel("Time")

st.pyplot(fig3)

# ---------------------------
# 🔥 Topic Extraction
# ---------------------------
st.subheader("🔥 Emerging Topics")

topic_extractor = TopicExtractor()
texts = load_recent_texts(ticker)

topics = topic_extractor.extract_topics(texts)

if topics:
    for topic in topics:
        st.markdown(f"- **{topic}**")
else:
    st.info("Not enough data to extract topics yet.")
