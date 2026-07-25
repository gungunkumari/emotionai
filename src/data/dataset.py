"""
Dataset loader for EmotionSense AI.
"""

from pathlib import Path

from torchvision.datasets import ImageFolder

from src.data.transforms import train_transforms, val_transforms


def get_datasets(data_dir: str):
    """
    Load train, validation, and test datasets.
    """

    data_path = Path(data_dir)

    train_dataset = ImageFolder(
        root=data_path / "train",
        transform=train_transforms,
    )

    val_dataset = ImageFolder(
        root=data_path / "val",
        transform=val_transforms,
    )

    test_dataset = ImageFolder(
        root=data_path / "test",
        transform=val_transforms,
    )

    return train_dataset, val_dataset, test_dataset