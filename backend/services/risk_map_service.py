import pandas as pd

from pathlib import Path
RISK_MAP_PATH = "https://agriguardai.blob.core.windows.net/data/merged_for_mapping_final.csv?sp=r&st=2026-07-07T20:51:25Z&se=2026-07-08T05:06:25Z&spr=https&sv=2026-02-06&sr=b&sig=8rtQpa6IUBJwHPvgHJxvPFxr3kG%2B4lbYfw2T8NbobE4%3D"
def get_risk_map_data():
    print(RISK_MAP_PATH)
    df = pd.read_csv(RISK_MAP_PATH)

    required_columns = [
        "Grid_ID",
        "date",
        "lat",
        "lon",
        "risk_label",
        "NDVI",
        "risk_score"
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing columns in risk map dataset: {missing_columns}")
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    optional_columns = ["NDWI", "EVI"]

    columns_to_return = required_columns + [
        col for col in optional_columns
        if col in df.columns
    ]

    df = df[columns_to_return].dropna(
        subset=[
            "Grid_ID",
            "date",
            "lat",
            "lon",
            "risk_label",
            "NDVI",
            "risk_score"
        ]
    )

    return df.to_dict(orient="records")