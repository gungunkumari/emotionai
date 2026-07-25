import os
import torch


class ModelCheckpoint:
    """
    Save the best model based on validation accuracy.
    """

    def __init__(self, save_dir="models/checkpoints"):

        self.best_accuracy = 0.0

        os.makedirs(save_dir, exist_ok=True)

        self.save_path = os.path.join(
            save_dir,
            "best_cnn.pth",
        )

    def __call__(self, model, accuracy):

        if accuracy > self.best_accuracy:

            self.best_accuracy = accuracy

            torch.save(
                model.state_dict(),
                self.save_path,
            )

            print(
                f"\n✅ New best model saved "
                f"(Validation Accuracy: {accuracy:.4f})"
            )