from dotenv import load_dotenv
import os
from google import genai
import xgboost as xgb
import pandas as pd
from pathlib import Path

load_dotenv()
        
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = xgb.XGBClassifier()

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "saved_models" / "xgb_model.json"

model = xgb.XGBClassifier()
model.load_model(MODEL_PATH)


def ask_ai(user_question, features):

    data = pd.DataFrame([features])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    risk = "High Risk" if prediction == 1 else "Healthy"

    prompt = f"""
You are an Agricultural AI Assistant.

Machine Learning Prediction:
- Risk Level: {risk}
- Stress Probability: {probability:.2%}

Input Features:
{features}

User Question:
{user_question}

Instructions:
- Explain the prediction based ONLY on the machine learning results.
- Give practical recommendations.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "risk": risk,
        "probability": float(probability),
        "prediction": int(prediction),
        "answer": response.text
    }