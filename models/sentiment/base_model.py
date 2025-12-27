from abc import ABC, abstractmethod

class BaseSentimentModel(ABC):

    @abstractmethod
    def predict(self, text: str) -> dict:
        """
        Returns:
        {
            "sentiment": "positive|neutral|negative",
            "confidence": float
        }
        """
        pass
