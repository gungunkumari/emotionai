import torch

from src.training.losses import get_loss_function

criterion = get_loss_function()

predictions = torch.randn(4, 7)

labels = torch.tensor([0, 1, 2, 3])

loss = criterion(predictions, labels)

print(loss)