from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load('models/churn_model.pkl')

class Customer(BaseModel):
    recency: int
    frequency: int
    monetary: float

# Add this root endpoint
@app.get("/")
def read_root():
    return {"status": "API is running", "endpoints": ["/predict_churn"]}

@app.post("/predict_churn")
def predict_churn(customer: Customer):
    prediction = model.predict([[customer.recency, customer.frequency, customer.monetary]])
    return {"churn_risk": int(prediction[0])}
