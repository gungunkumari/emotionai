from fastapi import APIRouter
from backend.app.schemas.response import HealthResponse

router = APIRouter(tags=["Health"])


@router.get("/")
def root():
    return {
        "message": "EmotionSense AI Backend Running"
    }


@router.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(status="healthy")