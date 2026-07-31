from pydantic import BaseModel


class PredictionRequest(BaseModel):
    filename: str