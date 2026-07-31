from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.db.database import get_db
from backend.app.models.prediction import Prediction

router = APIRouter(
    prefix="/predictions",
    tags=["Predictions"]
)

@router.get("/")
def get_predictions(db: Session = Depends(get_db)):
    predictions = (
        db.query(Prediction)
        .order_by(Prediction.created_at.desc())
        .all()
    )
    return predictions

@router.get("/{prediction_id}")
def get_prediction(prediction_id: int, db: Session = Depends(get_db)):
    prediction = (
        db.query(Prediction)
        .filter(Prediction.id == prediction_id)
        .first()
    )

    if prediction is None:
        raise HTTPException(status_code=404, detail="Prediction not found")

    return prediction

@router.delete("/{prediction_id}")
def delete_prediction(prediction_id: int, db: Session = Depends(get_db)):
    prediction = (
        db.query(Prediction)
        .filter(Prediction.id == prediction_id)
        .first()
    )

    if prediction is None:
        raise HTTPException(status_code=404, detail="Prediction not found")

    db.delete(prediction)
    db.commit()

    return {"message": "Prediction deleted successfully"}