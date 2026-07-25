from src.models.cnn import EmotionCNN
from src.models.resnet import EmotionResNet
from src.models.vit import EmotionViT


def build_model(config):

    name = config["model"]["name"].lower()

    if name == "cnn":
        return EmotionCNN()

    if name == "resnet18":
        return EmotionResNet()

    if name == "vit":
        return EmotionViT()

    raise ValueError(f"Unknown model {name}")