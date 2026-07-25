import torch

from src.models.cnn import EmotionCNN

model = EmotionCNN()

x = torch.randn(4, 3, 224, 224)

output = model(x)

print(model)
print(output.shape)