import pandas as pd

DATA_PATH = "https://agriguardai.blob.core.windows.net/data/merged_for_mapping_final.csv?sp=r&st=2026-07-07T20:51:25Z&se=2026-07-08T05:06:25Z&spr=https&sv=2026-02-06&sr=b&sig=..."

def get_dashboard_data():
    df = pd.read_csv(
        DATA_PATH,
        low_memory=False
    )

    df = df.tail(3000)

    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    ).dt.strftime("%Y-%m-%d")

    return df.to_dict(orient="records")