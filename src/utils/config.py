"""
Configuration loader for EmotionSense AI.
"""

from pathlib import Path

import yaml


def load_config(config_path: str) -> dict:
    """
    Load a YAML configuration file.

    Args:
        config_path: Path to the YAML configuration file.

    Returns:
        Dictionary containing configuration values.
    """
    config_file = Path(config_path)

    if not config_file.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_file, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config