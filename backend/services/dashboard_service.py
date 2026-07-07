import pandas as pd
import traceback

DATA_PATH = "https://agriguardai.blob.core.windows.net/data/merged_for_mapping_final.csv?sp=r&st=2026-07-07T22:28:05Z&se=2028-12-31T07:43:05Z&spr=https&sv=2026-02-06&sr=b&sig=Wg5rYEAC0thQIal5GahStNb7Oensk7sLOV1%2FqjOC0H0%3D"

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