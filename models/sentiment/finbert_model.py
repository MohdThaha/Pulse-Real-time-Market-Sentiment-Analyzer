from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

from models.sentiment.base_model import BaseSentimentModel
from utils.logger import setup_logger

logger = setup_logger(__name__)

class FinBERTSentimentModel(BaseSentimentModel):
    def __init__(self):
        logger.info("Loading FinBERT model...")
        self.tokenizer = AutoTokenizer.from_pretrained(
            "ProsusAI/finbert"
        )
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "ProsusAI/finbert"
        )
        self.model.eval()
        logger.info("FinBERT loaded successfully")

        self.labels = ["negative", "neutral", "positive"]

    def predict(self, text: str) -> dict:
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        with torch.no_grad():
            outputs = self.model(**inputs)
            probs = F.softmax(outputs.logits, dim=1)[0]

        confidence, idx = torch.max(probs, dim=0)

        return {
            "sentiment": self.labels[idx.item()],
            "confidence": round(confidence.item(), 4)
        }
