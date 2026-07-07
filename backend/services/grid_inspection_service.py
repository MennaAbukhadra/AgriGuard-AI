from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
GRID_DATA_PATH = BASE_DIR / "data" / "merged_for_mapping_final.csv"

df = pd.read_csv(GRID_DATA_PATH)
def get_grid_list():
    return sorted(df["Grid_ID"].astype(str).unique().tolist())

required_columns = [
    "Grid_ID",
    "date",
    "NDVI",
    "NDWI",
    "EVI",
    "veg_health",
    "temperature",
    "rainfall",
    "humidity",
    "VPD",
    "risk_score",
    "risk_label"
]

available_columns = [
    col for col in required_columns
    if col in df.columns
]

df = df[available_columns].copy()
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")


def get_grid_inspection_data(grid_id=None):

    if grid_id:
        result = df[df["Grid_ID"].astype(str) == str(grid_id)]
    else:
        result = df

    return result.to_dict(orient="records")