from fastapi import FastAPI, HTTPException
import os
from services.model_insights_service import get_model_insights
from services.risk_map_service import get_risk_map_data
from services.dashboard_service import get_dashboard_data
from services.grid_inspection_service import get_grid_inspection_data
from services.prediction_service import predict as predict_crop
from services.gemini_service import ask_ai
from schemas import PredictionInput as PredictionRequest
import traceback

print(__file__)
print(os.getcwd())

print("MAIN FILE LOADED")

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AgriGuard API is Running"}


@app.get("/dashboard")
def dashboard():
    import traceback
    try:
        return get_dashboard_data()
    except Exception:
        traceback.print_exc()
        raise


@app.get("/test")
def test():
    return {"ok": True}


@app.get("/risk-map")
def risk_map():
    try:
        return get_risk_map_data()
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"error": str(e)}

@app.get("/grid-inspection")
def grid_inspection(grid_id: str | None = None):
    return get_grid_inspection_data(grid_id)


@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        result = predict_crop(request.model_dump())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/model-insights")
def model_insights():
    return get_model_insights()
    
    
from services.gemini_service import ask_ai
from schemas import ChatRequest

@app.post("/chat")
def chat(request: ChatRequest):
    return ask_ai(
        request.question,
        request.features
    )
    
print("ROUTES:")
for route in app.routes:
    print(route.path)