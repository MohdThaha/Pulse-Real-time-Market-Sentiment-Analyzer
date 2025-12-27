📈 Pulse — Real-Time Market Sentiment Analyzer

Pulse is a real-time NLP system that ingests live social media data related to stock tickers, performs sentiment and topic analysis using transformer models, and visualizes market mood changes through an interactive dashboard.

Financial sentiment on social media often shifts minutes or hours before traditional news outlets, impacting stock prices rapidly. Pulse helps traders, analysts, and researchers detect sentiment spikes and emerging themes early.

---

🚀 Key Features

🔄 Live social data ingestion (Twitter/X via API)
🧠 Transformer-based sentiment analysis (FinBERT)
📊 Time-series sentiment tracking
🚨 Sentiment spike alerts
🔍 Keyword & topic extraction (KeyBERT)
📈 Real-time interactive dashboard (Streamlit)
🗃 Persistent time-series storage (SQLite)

---

🧩 Architecture Overview

Twitter/X API -> 

(Live Tweets) -> 

Ingestion Service (Python) -> 

Cleaned Text -> 

Sentiment API (FastAPI + FinBERT) -> 

Sentiment + Confidence -> 

Time-Series Storage (SQLite) -> 

Topic Extraction (KeyBERT) -> 

Streamlit Dashboard (Live Visualization)


---

🛠 Tech Stack
Layer	Tools
Language	Python 3.13
NLP Models	FinBERT, KeyBERT
ML Framework	Hugging Face Transformers
API	FastAPI
Dashboard	Streamlit
Storage	SQLite
Visualization	Matplotlib
Data Source	Twitter/X (RapidAPI)

---

📊 Dashboard Capabilities

Sentiment over time (raw + rolling average)
Tweet volume spikes
Sentiment distribution
Real-time market alerts
Emerging discussion topics per ticker
Multi-ticker support (AAPL, TSLA, NVDA, MSFT)

---

⚠️ Example Use Case

A sudden surge in negative sentiment for a stock ticker appears on Twitter.
Pulse detects a sharp sentiment drop, highlights emerging negative keywords, and alerts the user before major news outlets publish the story.

---

▶️ How to Run Locally
# 1. Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start Sentiment API
uvicorn api.main:app --host 127.0.0.1 --port 8000

# 4. Run ingestion
python -m ingestion.ingest_manager

# 5. Launch dashboard
streamlit run dashboard/app.py

---

🧠 What This Project Demonstrates

Real-time ML pipelines
Transformer-based NLP
Production-style API design
Streaming data ingestion
Time-series analytics
End-to-end ML system thinking

---

🔮 Future Improvements

Redis/Kafka for streaming

ElasticSearch for search

Topic trend persistence

Slack/email alerts

Deployment on AWS/GCP

---

👤 Author

Mohammed Thaha Dawood
AI / Backend / ML Engineer
📍 India