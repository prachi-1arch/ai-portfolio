from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np

app = FastAPI(title="Customer Churn Prediction API", version="1.0.0")

# Simulated model (replace with actual joblib.load)
class ChurnModel:
    def predict_proba(self, features):
        # Dummy prediction for demo
        score = np.random.uniform(0.1, 0.9)
        return np.array([[1 - score, score]])

model = ChurnModel()

class CustomerData(BaseModel):
    tenure: float
    monthly_charges: float
    total_charges: float
    contract: str = "Month-to-month"
    payment_method: str = "Electronic check"

@app.get("/")
def root():
    return {"message": "Customer Churn Prediction API", "version": "1.0.0"}

@app.post("/predict")
def predict(customer: CustomerData):
    try:
        features = np.array([[customer.tenure, customer.monthly_charges, customer.total_charges]])
        prediction = model.predict_proba(features)[0]
        
        return {
            "churn_probability": round(float(prediction[1]), 3),
            "retain_probability": round(float(prediction[0]), 3),
            "risk_level": "High" if prediction[1] > 0.7 else "Medium" if prediction[1] > 0.4 else "Low",
            "input": customer.dict()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "healthy", "model": "churn-v1"}

# Run with: uvicorn app:app --reload
