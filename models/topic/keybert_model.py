from keybert import KeyBERT
from sentence_transformers import SentenceTransformer
import torch

class TopicExtractor:
    def __init__(self):
        # Force CPU + eager loading (fixes meta tensor issue)
        embedding_model = SentenceTransformer(
            "all-MiniLM-L6-v2",
            device="cpu"
        )

        self.model = KeyBERT(model=embedding_model)

    def extract_topics(self, texts, top_n=5):
        if not texts:
            return []

        combined_text = " ".join(texts)

        keywords = self.model.extract_keywords(
            combined_text,
            keyphrase_ngram_range=(1, 2),
            stop_words="english",
            top_n=top_n
        )

        return keywords
