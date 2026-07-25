import matplotlib.pyplot as plt


def plot_history(history):

    plt.figure(figsize=(8,5))

    plt.plot(history["train_loss"])

    plt.plot(history["val_loss"])

    plt.legend(["Train","Validation"])

    plt.title("Loss Curve")

    plt.savefig("loss_curve.png")

    plt.close()

    plt.figure(figsize=(8,5))

    plt.plot(history["train_acc"])

    plt.plot(history["val_acc"])

    plt.legend(["Train","Validation"])

    plt.title("Accuracy Curve")

    plt.savefig("accuracy_curve.png")

    plt.close()