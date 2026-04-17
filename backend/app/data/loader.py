from google.cloud import bigquery
import pandas as pd

PROJECT_ID = "veerababu33"
DATASET_ID = "career_analytics"

MERGED_TABLE = f"`{PROJECT_ID}.{DATASET_ID}.merged_career_dataset`"
OCCUPATIONS_TABLE = f"`{PROJECT_ID}.{DATASET_ID}.occupations_clean`"


def _run_query(query: str) -> pd.DataFrame:
    client = bigquery.Client(project=PROJECT_ID)
    rows = client.query(query).result()
    data = [dict(row.items()) for row in rows]
    return pd.DataFrame(data)


def load_merged_data():
    query = f"""
    SELECT *
    FROM {MERGED_TABLE}
    """
    return _run_query(query)


def load_occupations_data():
    query = f"""
    SELECT *
    FROM {OCCUPATIONS_TABLE}
    """
    return _run_query(query)