import torch
from PIL import Image
from torchvision import transforms

from src.models.model_factory import build_model


class EmotionPredictor:

    def __init__(self, config):

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.model = build_model(config)

        checkpoint = torch.load(
            config["model"]["checkpoint"],
            map_location=self.device,
        )

        self.model.load_state_dict(checkpoint)

        self.model.to(self.device)

        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
        ])

        self.classes = [
            "Angry",
            "Disgust",
            "Fear",
            "Happy",
            "Neutral",
            "Sad",
            "Surprise",
        ]

    def predict(self, image_path):

        image = Image.open(image_path).convert("RGB")

        tensor = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():

            output = self.model(tensor)

            probs = torch.softmax(output, dim=1)

            confidence, pred = torch.max(probs, dim=1)

        return {
            "emotion": self.classes[pred.item()],
            "confidence": round(confidence.item() * 100, 2),
        }