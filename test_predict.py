from src.utils.config import load_config
from src.inference.predictor import EmotionPredictor

config = load_config("configs/cnn.yaml")

predictor = EmotionPredictor(config)

result = predictor.predict("sample.jpg")

print(result)