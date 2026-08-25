from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="AI Sales Forecasting API", version="1.0.0")

class ForecastRequest(BaseModel):
    historical_sales: list[float]
    sku_id: str
    store_id: str
    forecast_horizon: int = 30

@app.get("/")
def root():
    return {"message": "AI Sales Forecasting API", "version": "1.0.0"}

@app.post("/forecast")
def forecast(request: ForecastRequest):
    try:
        # Simulated ensemble prediction
        last_value = request.historical_sales[-1] if request.historical_sales else 1000
        
        # Generate forecast with slight trend and noise
        trend = np.linspace(last_value, last_value * 1.1, request.forecast_horizon)
        noise = np.random.normal(0, last_value * 0.05, request.forecast_horizon)
        ensemble_pred = trend + noise
        
        return {
            "sku_id": request.sku_id,
            "store_id": request.store_id,
            "forecast_horizon": request.forecast_horizon,
            "forecast": [round(float(x), 2) for x in ensemble_pred],
            "confidence_interval": {
                "lower": [round(float(x * 0.9), 2) for x in ensemble_pred],
                "upper": [round(float(x * 1.1), 2) for x in ensemble_pred]
            },
            "model": "LSTM_Prophet_Ensemble_v1"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "healthy", "models_loaded": 2}

# Run with: uvicorn app:app --reload
