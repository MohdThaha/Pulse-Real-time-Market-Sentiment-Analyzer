from keybert import KeyBERT

class TopicExtractor:
    def __init__(self):
        self.model = KeyBERT("all-MiniLM-L6-v2")

    def extract_topics(self, texts, top_n=5):
        """
        texts: list[str]
        returns: list[str]
        """
        if not texts:
            return []

        joined_text = " ".join(texts)

        keywords = self.model.extract_keywords(
            joined_text,
            keyphrase_ngram_range=(1, 2),
            stop_words="english",
            top_n=top_n
        )

        return [kw for kw, score in keywords]
