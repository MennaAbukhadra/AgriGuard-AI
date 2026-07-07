import pandas as pd
import traceback

DATA_PATH = "https://agriguardai.blob.core.windows.net/data/merged_for_mapping_final.csv"

try:
    print("Loading dashboard dataset...")
    print(DATA_PATH)

    df = pd.read_csv(
        DATA_PATH,
        low_memory=False
    )

    print(f"Dataset loaded successfully: {df.shape}")

    df = df.tail(3000)

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    ).dt.strftime("%Y-%m-%d")

    print("Dashboard dataset ready.")

except Exception:
    print("ERROR LOADING DASHBOARD DATASET")
    traceback.print_exc()
    raise


def get_dashboard_data():
    return df.to_dict(orient="records")