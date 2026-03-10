
# Mining Intelligence Platform (Enterprise Scaffold)

A multi-service mining intelligence platform including:

- FastAPI backend API
- React enterprise dashboard
- ML predictive maintenance service
- Telemetry simulator
- Docker compose for local orchestration

Architecture:

backend/api           → Core platform API  
ml-engine/service     → Predictive maintenance model service  
telemetry/simulator   → Equipment telemetry generator  
frontend/dashboard    → React enterprise dashboard UI  

Run locally:

Backend:
pip install -r backend/api/requirements.txt
python backend/api/app.py

ML Service:
pip install -r ml-engine/service/requirements.txt
python ml-engine/service/ml_service.py

Telemetry Simulator:
python telemetry/simulator/producer.py

Frontend:
cd frontend/dashboard
npm install
npm start
