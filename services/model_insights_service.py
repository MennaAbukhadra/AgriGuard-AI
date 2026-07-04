import os
import joblib
import xgboost as xgb

MODEL_DIR = "saved_models"

model = xgb.XGBClassifier()
model.load_model(os.path.join(MODEL_DIR, "xgb_model.json"))

feature_names = joblib.load(
    os.path.join(MODEL_DIR, "feature_names.pkl")
)


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