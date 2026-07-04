import pandas as pd

RISK_MAP_PATH = "merged_for_mapping_final.csv"

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