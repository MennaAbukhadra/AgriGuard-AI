from pydantic import BaseModel

class PredictionInput(BaseModel):
    NDVI: float
    veg_health: float
    EVI_change: float
    water_stress: int
    heat_stress: int
    dry_stress: int
    VPD_stress: int
    drought_severity: float
    

from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str

    features: dict