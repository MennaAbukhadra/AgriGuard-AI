import joblib
import xgboost as xgb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "saved_models" / "xgb_model.json"
FEATURES_PATH = BASE_DIR / "saved_models" / "feature_names.pkl"

model = xgb.XGBClassifier()
model.load_model(MODEL_PATH)

feature_names = joblib.load(FEATURES_PATH)


def get_model_insights():

    feature_importance = []

    for feature, importance in zip(
        feature_names,
        model.feature_importances_
    ):
        feature_importance.append({
            "feature": feature,
            "importance": round(float(importance), 4)
        })

    feature_importance = sorted(
        feature_importance,
        key=lambda x: x["importance"],
        reverse=True
    )

    return {
        "model": "XGBoost",
        "accuracy": 0.93,
        "precision": 0.53,
        "recall": 0.75,
        "f1_score": 0.62,
        "roc_auc": 0.96,
        "feature_importance": feature_importance
    }