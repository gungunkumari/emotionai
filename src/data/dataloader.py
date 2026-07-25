"""
DataLoader utilities for EmotionSense AI.
"""

from torch.utils.data import DataLoader

from src.data.dataset import get_datasets


def get_dataloaders(
    data_dir: str,
    batch_size: int = 32,
    num_workers: int = 0,
):
    """
    Create train, validation, and test DataLoaders.
    """

    train_dataset, val_dataset, test_dataset = get_datasets(data_dir)

    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        pin_memory=False,
    )

    val_loader = DataLoader(
        val_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=True,
    )

    test_loader = DataLoader(
        test_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=True,
    )

    return train_loader, val_loader, test_loader