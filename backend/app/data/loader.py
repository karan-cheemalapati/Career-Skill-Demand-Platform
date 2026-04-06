from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[3]
CLEANED_DATA_DIR = BASE_DIR / "data" / "cleaned_data"

MERGED_DATA_PATH = CLEANED_DATA_DIR / "merged_career_dataset.csv"
OCCUPATIONS_DATA_PATH = CLEANED_DATA_DIR / "occupations_clean.csv"


def load_merged_data():
    return pd.read_csv(MERGED_DATA_PATH)


def load_occupations_data():
    return pd.read_csv(OCCUPATIONS_DATA_PATH)