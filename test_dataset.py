from src.data.dataset import get_datasets

train_dataset, val_dataset, test_dataset = get_datasets(
    "data/raw/fer2013"
)

print(f"Train images: {len(train_dataset)}")
print(f"Validation images: {len(val_dataset)}")
print(f"Test images: {len(test_dataset)}")

print(train_dataset.classes)