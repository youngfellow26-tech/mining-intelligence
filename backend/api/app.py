from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI(
    title="Mining Intelligence API",
    description="InterMineForce360 Mining Intelligence Platform",
    version="1.0"
)

# -------------------------
# ROOT ENDPOINT
# -------------------------

@app.get("/")
def root():
    return {"status": "Mining Intelligence API running"}

# -------------------------
# HEALTHCHECK (Railway)
# -------------------------

@app.get("/health")
def health():
    return {"status": "ok"}

# -------------------------
# SYSTEM STATUS
# -------------------------

@app.get("/system")
def system_status():
    return {
        "api": "running",
        "ml_engine": "ready",
        "database": "not_connected"
    }

# -------------------------
# DATA MODELS
# -------------------------

class Telemetry(BaseModel):
    equipment_id: str
    temperature: float
    vibration: float
    fuel_level: float


class PredictionInput(BaseModel):
    load: float
    speed: float
    temperature: float

# -------------------------
# TELEMETRY INGESTION
# -------------------------

@app.post("/telemetry")
def receive_telemetry(data: Telemetry):

    anomaly = False

    if data.temperature > 95:
        anomaly = True

    if data.vibration > 8:
        anomaly = True

    return {
        "equipment_id": data.equipment_id,
        "anomaly_detected": anomaly,
        "message": "Telemetry processed"
    }

# -------------------------
# ML PREDICTION
# -------------------------

@app.post("/predict")
def predict(data: PredictionInput):

    values = np.array([
        data.load,
        data.speed,
        data.temperature
    ])

    score = values.mean()

    risk = "low"

    if score > 70:
        risk = "high"
    elif score > 40:
        risk = "medium"

    return {
        "prediction": "equipment_failure_risk",
        "risk_level": risk,
        "score": float(score)
    }

# -------------------------
# PLATFORM INFO
# -------------------------

@app.get("/info")
def info():
    return {
        "platform": "InterMineForce360",
        "version": "1.0",
        "modules": [
            "telemetry",
            "prediction",
            "system_monitoring"
        ]
    }
