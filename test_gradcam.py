import torch
from PIL import Image
from torchvision import transforms

from src.models.resnet import EmotionResNet
from src.explainability.gradcam import EmotionGradCAM
from src.utils.image_utils import save_image


model = EmotionResNet()

model.load_state_dict(
    torch.load(
        "models/checkpoints/best_cnn.pth",
        map_location="cpu",
    )
)

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

image = Image.open("sample.jpg").convert("RGB")

tensor = transform(image).unsqueeze(0)

cam = EmotionGradCAM(
    model,
    model.model.layer4[-1],
)

heatmap = cam.generate(tensor)

save_image(
    "gradcam_output.jpg",
    heatmap,
)

print("GradCAM saved.")