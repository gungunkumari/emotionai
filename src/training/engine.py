import torch
from tqdm import tqdm

from src.training.metrics import calculate_metrics


def train_one_epoch(model, dataloader, criterion, optimizer, device):
    model.train()

    running_loss = 0.0

    all_outputs = []
    all_labels = []

    for images, labels in tqdm(
        dataloader,
        desc="Training",
        leave=False,
    ):

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

        all_outputs.append(outputs.detach().cpu())
        all_labels.append(labels.detach().cpu())

    outputs = torch.cat(all_outputs)
    labels = torch.cat(all_labels)

    metrics = calculate_metrics(outputs, labels)

    epoch_loss = running_loss / len(dataloader)

    return epoch_loss, metrics


def validate_one_epoch(model, dataloader, criterion, device):

    model.eval()

    running_loss = 0.0

    all_outputs = []
    all_labels = []

    with torch.no_grad():

        for images, labels in tqdm(
            dataloader,
            desc="Validation",
            leave=False,
        ):

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            loss = criterion(outputs, labels)

            running_loss += loss.item()

            all_outputs.append(outputs.cpu())
            all_labels.append(labels.cpu())

    outputs = torch.cat(all_outputs)
    labels = torch.cat(all_labels)

    metrics = calculate_metrics(outputs, labels)

    epoch_loss = running_loss / len(dataloader)

    return epoch_loss, metrics