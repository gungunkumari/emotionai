from collections import Counter

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.db.database import get_db
from backend.app.models.prediction import Prediction

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/stats")
def get_dashboard_stats(db: Session = Depends(get_db)):
    predictions = db.query(Prediction).all()

    total_predictions = len(predictions)

    if total_predictions == 0:
        return {
            "total_predictions": 0,
            "average_confidence": 0,
            "emotion_counts": {},
            "latest_prediction": None
        }

    average_confidence = round(
        sum(p.confidence for p in predictions) / total_predictions,
        2
    )

    emotion_counts = dict(
        Counter(p.emotion for p in predictions)
    )

    latest = max(predictions, key=lambda p: p.created_at)

    return {
        "total_predictions": total_predictions,
        "average_confidence": average_confidence,
        "emotion_counts": emotion_counts,
        "latest_prediction": {
            "filename": latest.filename,
            "emotion": latest.emotion,
            "confidence": latest.confidence,
            "created_at": latest.created_at
        }
    }