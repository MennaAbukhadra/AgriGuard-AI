import pandas as pd
import xgboost as xgb
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "saved_models" / "xgb_model.json"
FEATURES_PATH = BASE_DIR / "saved_models" / "feature_names.pkl"

feature_names = joblib.load(FEATURES_PATH)

model = xgb.XGBClassifier()
model.load_model(MODEL_PATH)


def _to_dict(data):
    if isinstance(data, dict):
        return data

    if hasattr(data, "model_dump"):
        return data.model_dump()

    if hasattr(data, "dict"):
        return data.dict()

    return {
        feature: getattr(data, feature)
        for feature in feature_names
    }


def predict(data):
    data = _to_dict(data)

    missing_features = [
        feature for feature in feature_names
        if feature not in data
    ]

    if missing_features:
        raise ValueError(f"Missing features: {', '.join(missing_features)}")

    df = pd.DataFrame([
        {
            feature: data[feature]
            for feature in feature_names
        }
    ])

    df = df.apply(pd.to_numeric, errors="coerce")

    invalid_features = df.columns[df.isna().any()].tolist()

    if invalid_features:
        raise ValueError(
            f"Invalid numeric values for: {', '.join(invalid_features)}"
        )

    df = df.astype("float32")

    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][1])

    return {
        "prediction": prediction,
        "probability": probability,
        "probability_percent": round(probability * 100, 2),
        "risk_level": "High" if prediction else "Low",
        "status": "Stressed" if prediction else "Healthy"
    }