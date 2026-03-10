
from fastapi import FastAPI
import os

app = FastAPI(title="Mining Intelligence Platform")

@app.get("/")
def root():
    return {"platform": "Mining Intelligence Platform", "status": "online"}

@app.get("/fleet")
def fleet():
    return [
        {"equipment": "Truck-101", "status": "operational", "location": "Pit A"},
        {"equipment": "Drill-22", "status": "maintenance", "location": "Pit B"},
        {"equipment": "Excavator-9", "status": "operational", "location": "Pit C"},
    ]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
