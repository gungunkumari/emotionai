import torch

from src.training.engine import train_one_epoch, validate_one_epoch
from src.training.callbacks import ModelCheckpoint


def train_model(
    model,
    train_loader,
    val_loader,
    criterion,
    optimizer,
    device,
    epochs,
):

    history = {
        "train_loss": [],
        "val_loss": [],
        "train_acc": [],
        "val_acc": [],
    }

    model.to(device)

    # Initialize checkpoint saver
    checkpoint = ModelCheckpoint()

    for epoch in range(epochs):

        train_loss, train_metrics = train_one_epoch(
            model,
            train_loader,
            criterion,
            optimizer,
            device,
        )

        val_loss, val_metrics = validate_one_epoch(
            model,
            val_loader,
            criterion,
            device,
        )

        # Save history
        history["train_loss"].append(train_loss)
        history["val_loss"].append(val_loss)

        history["train_acc"].append(train_metrics["accuracy"])
        history["val_acc"].append(val_metrics["accuracy"])

        # Save the best model
        checkpoint(
            model,
            val_metrics["accuracy"],
        )

        print(f"\nEpoch {epoch + 1}/{epochs}")

        print(
            f"Train Loss: {train_loss:.4f} | "
            f"Train Acc: {train_metrics['accuracy']:.4f}"
        )

        print(
            f"Val Loss: {val_loss:.4f} | "
            f"Val Acc: {val_metrics['accuracy']:.4f}"
        )

    return history