"""
Evaluation metrics for EmotionSense AI.
"""

import torch
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)


def calculate_metrics(outputs, labels):
    """
    Calculate Accuracy, Precision, Recall and F1 Score.
    """

    predictions = torch.argmax(outputs, dim=1)

    y_true = labels.cpu().numpy()
    y_pred = predictions.cpu().numpy()

    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        ),
        "recall": recall_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        ),
        "f1": f1_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        ),
    }

    return metrics