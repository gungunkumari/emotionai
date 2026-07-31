from pathlib import Path

from src.inference.predictor import EmotionPredictor
from src.utils.config import load_config


class PredictorService:
    """
    Service responsible for loading the trained model
    and performing emotion prediction.
    """

    def __init__(self):
        config_path = Path("configs/cnn.yaml")
        config = load_config(config_path)

        self.predictor = EmotionPredictor(config)

    def predict(self, image_path: str):
        return self.predictor.predict(image_path)