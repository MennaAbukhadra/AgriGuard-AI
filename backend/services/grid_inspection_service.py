import pandas as pd

GRID_DATA_PATH = "https://agriguardai.blob.core.windows.net/data/merged_for_mapping_final.csv?sp=r&st=2026-07-07T22:28:05Z&se=2028-12-31T07:43:05Z&spr=https&sv=2026-02-06&sr=b&sig=Wg5rYEAC0thQIal5GahStNb7Oensk7sLOV1%2FqjOC0H0%3D"

print("Loading Grid Inspection dataset...")

df = pd.read_csv(
    GRID_DATA_PATH,
    low_memory=False
)

print("Grid Inspection dataset loaded.")

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

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
).dt.strftime("%Y-%m-%d")


def get_grid_list():
    return sorted(df["Grid_ID"].astype(str).unique().tolist())


def get_grid_inspection_data(grid_id=None):
    if grid_id:
        result = df[df["Grid_ID"].astype(str) == str(grid_id)]
    else:
        result = df

    return result.to_dict(orient="records")