from fastapi import APIRouter
from api.schemas.request import SentimentRequest
from api.schemas.response import SentimentResponse
from api.services.inference_service import inference_service

router = APIRouter()

@router.post("/predict", response_model=SentimentResponse)
def predict_sentiment(request: SentimentRequest):
    result = inference_service.analyze(request.text)

    return SentimentResponse(
        sentiment=result["sentiment"],
        confidence=result["confidence"]
    )
