from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

from backend.app.db.database import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    emotion = Column(String, nullable=False)

    confidence = Column(Float, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )