from src.data.dataloader import get_dataloaders


def main():
    train_loader, val_loader, test_loader = get_dataloaders(
        "data/raw/fer2013",
        batch_size=32,
        num_workers=0,
    )

    images, labels = next(iter(train_loader))

    print("Image batch shape:", images.shape)
    print("Label batch shape:", labels.shape)
    print("Labels:", labels[:10])


if __name__ == "__main__":
    main()