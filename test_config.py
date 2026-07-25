from src.utils.config import load_config

config = load_config("configs/cnn.yaml")

print(config)
print(config["training"]["epochs"])
print(config["model"]["name"])