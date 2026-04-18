from google.cloud import bigquery
from google.oauth2 import service_account
from pathlib import Path
import pandas as pd

PROJECT_ID = "veerababu33"
DATASET_ID = "career_analytics"

MERGED_TABLE = f"`{PROJECT_ID}.{DATASET_ID}.merged_career_dataset`"
OCCUPATIONS_TABLE = f"`{PROJECT_ID}.{DATASET_ID}.occupations_clean`"

KEY_PATH = Path(__file__).resolve().parent.parent / "gcp-key.json"

_merged_cache = None
_occupations_cache = None


def _get_bigquery_client():
    credentials = service_account.Credentials.from_service_account_file(
        str(KEY_PATH)
    )
    return bigquery.Client(project=PROJECT_ID, credentials=credentials)


def _run_query(query: str) -> pd.DataFrame:
    client = _get_bigquery_client()
    rows = client.query(query).result()
    data = [dict(row.items()) for row in rows]
    return pd.DataFrame(data)


def load_merged_data(force_refresh: bool = False):
    global _merged_cache

    if _merged_cache is None or force_refresh:
        query = f"""
        SELECT *
        FROM {MERGED_TABLE}
        """
        _merged_cache = _run_query(query)

    return _merged_cache.copy()


def load_occupations_data(force_refresh: bool = False):
    global _occupations_cache

    if _occupations_cache is None or force_refresh:
        query = f"""
        SELECT *
        FROM {OCCUPATIONS_TABLE}
        """
        _occupations_cache = _run_query(query)

    return _occupations_cache.copy()

def clear_data_cache():
    global _merged_cache, _occupations_cache
    _merged_cache = None
    _occupations_cache = None
    
    