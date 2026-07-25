from torch.optim.lr_scheduler import StepLR


def get_scheduler(optimizer):
    """
    Returns the learning rate scheduler.
    """

    scheduler = StepLR(
        optimizer,
        step_size=5,
        gamma=0.1,
    )

    return scheduler