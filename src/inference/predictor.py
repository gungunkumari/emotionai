import torch
from PIL import Image
from torchvision import transforms

from src.models.model_factory import build_model
from backend.app.services.gradcam_service import GradCAMService


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

        # Initialize Grad-CAM
        self.gradcam = GradCAMService(self.model)

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

        # Required for Grad-CAM
        tensor = tensor.clone().detach().requires_grad_(True)

        output = self.model(tensor)

        probs = torch.softmax(output, dim=1)

        confidence, pred = torch.max(probs, dim=1)

        # Generate Grad-CAM heatmap
        gradcam_path = self.gradcam.generate(
            input_tensor=tensor,
            predicted_class=pred.item(),
            original_image_path=image_path,
        )

        return {
            "emotion": self.classes[pred.item()],
            "confidence": round(confidence.item() * 100, 2),
            "gradcam_image": gradcam_path,
        }