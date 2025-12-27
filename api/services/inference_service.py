from models.sentiment.finbert_model import FinBERTSentimentModel
from utils.logger import setup_logger

logger = setup_logger(__name__)

class InferenceService:
    def __init__(self):
        self.model = FinBERTSentimentModel()

    def analyze(self, text: str) -> dict:
        return self.model.predict(text)


# Singleton instance
inference_service = InferenceService()
