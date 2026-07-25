from torch.utils.tensorboard import SummaryWriter


class TensorBoardLogger:

    def __init__(self):

        self.writer = SummaryWriter("runs/emotion_ai")

    def log(self, epoch, train_loss, val_loss, train_acc, val_acc):

        self.writer.add_scalar(
            "Loss/Train",
            train_loss,
            epoch,
        )

        self.writer.add_scalar(
            "Loss/Validation",
            val_loss,
            epoch,
        )

        self.writer.add_scalar(
            "Accuracy/Train",
            train_acc,
            epoch,
        )

        self.writer.add_scalar(
            "Accuracy/Validation",
            val_acc,
            epoch,
        )

    def close(self):

        self.writer.close()