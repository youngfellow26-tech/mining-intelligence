
from fastapi import FastAPI
import random

app = FastAPI(title="Predictive Maintenance AI")

@app.get("/predict/{machine}")
def predict(machine: str):
    risk = random.uniform(0,1)
    return {
        "machine": machine,
        "failure_risk": round(risk,2),
        "recommendation": "schedule maintenance" if risk > 0.6 else "normal operation"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
