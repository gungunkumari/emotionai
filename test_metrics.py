import torch

from src.training.metrics import calculate_metrics

outputs = torch.randn(8, 7)

labels = torch.tensor([0, 1, 2, 3, 4, 5, 6, 1])

metrics = calculate_metrics(outputs, labels)

print(metrics)