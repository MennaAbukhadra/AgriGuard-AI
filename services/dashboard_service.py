import pandas as pd

df = pd.read_csv("merged_for_mapping_final.csv")
df["date"] = pd.to_datetime(df["date"])

def get_dashboard_data():
    return df.to_dict(orient="records")