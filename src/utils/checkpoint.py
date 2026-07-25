"""
Checkpoint utilities for saving and loading PyTorch models.
"""

from pathlib import Path

import torch


def save_checkpoint(state: dict, checkpoint_path: str) -> None:
    """
    Save a training checkpoint.

    Args:
        state: Dictionary containing model state.
        checkpoint_path: Path to save the checkpoint.
    """
    checkpoint_file = Path(checkpoint_path)
    checkpoint_file.parent.mkdir(parents=True, exist_ok=True)

    torch.save(state, checkpoint_file)


def load_checkpoint(checkpoint_path: str, device: str = "cpu") -> dict:
    """
    Load a training checkpoint.

    Args:
        checkpoint_path: Path to the checkpoint.
        device: Device to load the checkpoint onto.

    Returns:
        Loaded checkpoint dictionary.
    """
    checkpoint_file = Path(checkpoint_path)

    if not checkpoint_file.exists():
        raise FileNotFoundError(
            f"Checkpoint not found: {checkpoint_path}"
        )

    checkpoint = torch.load(
        checkpoint_file,
        map_location=device,
    )

    return checkpoint