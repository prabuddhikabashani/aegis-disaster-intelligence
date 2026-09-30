"""
Aegis - Data Download

This script will be used to download and prepare
the datasets required for the flood-risk ML model.
"""

from pathlib import Path


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data directories
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"
EXTERNAL_DATA_DIR = PROJECT_ROOT / "data" / "external"


def create_data_directories():
    """Create the required data directories."""

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    EXTERNAL_DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Data directories are ready.")


if __name__ == "__main__":
    create_data_directories()