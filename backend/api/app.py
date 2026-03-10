from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI(
    title="Mining Intelligence API",
    description="InterMineForce360 Mining Intelligence Platform",
    version="1.0"
)

# -----------------------------
# Models
# -----------------------------

class Telemetry(BaseModel):
    equipment_id: str
    temperature: float
    vibration: float
    fuel_level: float


class PredictionInput(BaseModel):
    load: float
    speed: float
    temperature: float


# -----------------------------
# Root Endpoint
# -----------------------------

@app.get("/")
def root():
    return {
        "platform": "InterMineForce360",
        "status": "running",
        "service": "Mining Intelligence API"
    }


# -----------------------------
# Health Check (Railway uses this)
# -----------------------------

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "api"
    }


# -----------------------------
# System Status
# -----------------------------

@app.get("/system")
def system_status():
    return {
        "api": "running",
        "ml_engine": "ready",
        "database": "simulated"
    }


# -----------------------------
# Telemetry Ingestion
# -----------------------------

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


# -----------------------------
# ML Prediction (demo)
# -----------------------------

@app.post("/predict")
def predict(data: PredictionInput):

    values = np.array([data.load, data.speed, data.temperature])
    
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


# -----------------------------
# API Info
# -----------------------------

@app.get("/info")
def api_info():
    return {
        "platform": "InterMineForce360",
        "version": "1.0",
        "modules": [
            "telemetry",
            "ml_prediction",
            "system_monitoring"
        ]
    }
