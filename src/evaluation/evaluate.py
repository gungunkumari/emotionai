import torch
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
)


def evaluate(model, dataloader, device):

    model.eval()

    predictions = []
    labels = []

    with torch.no_grad():

        for images, target in dataloader:

            images = images.to(device)

            outputs = model(images)

            pred = torch.argmax(outputs, dim=1)

            predictions.extend(pred.cpu().numpy())

            labels.extend(target.numpy())

    print(classification_report(labels, predictions))

    print(confusion_matrix(labels, predictions))