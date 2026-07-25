"""
Loss functions for EmotionSense AI.
"""

import torch.nn as nn


def get_loss_function():
    """
    Returns the loss function used for training.
    """
    return nn.CrossEntropyLoss()