import timm
import torch.nn as nn


class EmotionViT(nn.Module):

    def __init__(self, num_classes=7):

        super().__init__()

        self.model = timm.create_model(
            "vit_base_patch16_224",
            pretrained=True,
            num_classes=num_classes,
        )

        self.model.head = nn.Sequential(
            nn.Dropout(0.3),
            nn.Linear(
                self.model.head.in_features,
                num_classes,
            ),
        )

    def forward(self, x):
        return self.model(x)