from sqlalchemy.orm import Session
from backend.app.models.prediction import Prediction


class PredictionService:

    @staticmethod
    def create_prediction(
        db: Session,
        filename: str,
        emotion: str,
        confidence: float
    ):
        prediction = Prediction(
            filename=filename,
            emotion=emotion,
            confidence=confidence
        )

        db.add(prediction)
        db.commit()
        db.refresh(prediction)

        return prediction