import torch.nn as nn
from torchvision.models import resnet18, ResNet18_Weights


class EmotionResNet(nn.Module):

    def __init__(self, num_classes=7):

        super().__init__()

        self.model = resnet18(weights=ResNet18_Weights.DEFAULT)

        self.model.fc = nn.Linear(
            self.model.fc.in_features,
            num_classes,
        )

    def forward(self, x):

        return self.model(x)