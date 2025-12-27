from fastapi import FastAPI
from api.routes import health, sentiment
from api.services.inference_service import inference_service
from utils.logger import setup_logger

logger = setup_logger(__name__)

app = FastAPI(
    title="Pulse Sentiment API",
    version="1.0.0",
    description="Real-time market sentiment inference using FinBERT"
)

app.include_router(health.router)
app.include_router(sentiment.router)

@app.on_event("startup")
def warmup_model():
    logger.info("Warming up FinBERT model...")
    try:
        inference_service.analyze("Market sentiment warmup")
        logger.info("FinBERT warmup completed")
    except Exception as e:
        logger.error(f"Model warmup failed: {e}")

logger.info("Pulse Sentiment API initialized")
