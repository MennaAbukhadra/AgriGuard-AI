import pandas as pd

DATA_PATH = "https://agriguardai.blob.core.windows.net/data/merged_for_mapping_final.csv?sp=r&st=2026-07-07T20:51:25Z&se=2026-07-08T05:06:25Z&spr=https&sv=2026-02-06&sr=b&sig=8rtQpa6IUBJwHPvgHJxvPFxr3kG%2B4lbYfw2T8NbobE4%3D"


def get_dashboard_data():
    chunks = []

    for chunk in pd.read_csv(
        DATA_PATH,
        chunksize=5000,
        low_memory=False
    ):
        if "date" in chunk.columns:
            chunk["date"] = (
                pd.to_datetime(chunk["date"], errors="coerce")
                .dt.strftime("%Y-%m-%d")
            )
        chunks.append(chunk)

    df = pd.concat(chunks, ignore_index=True)

    return df.to_dict(orient="records")