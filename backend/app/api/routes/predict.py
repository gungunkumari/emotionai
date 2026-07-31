from pathlib import Path
import shutil
import uuid

from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session

from backend.app.db.database import get_db
from backend.app.services.predictor_service import PredictorService
from backend.app.services.prediction_service import PredictionService

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)

predictor_service = PredictorService()


@router.post("/")
async def predict(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)

    file_path = upload_dir / f"{uuid.uuid4()}_{file.filename}"

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        result = predictor_service.predict(str(file_path))

        PredictionService.create_prediction(
            db=db,
            filename=file.filename,
            emotion=result["emotion"],
            confidence=result["confidence"]
        )

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if file_path.exists():
            file_path.unlink()