from fastapi import FastAPI
import pandas as pd
import numpy as np
import joblib  # Assuming you're using a saved model


app = FastAPI()


# Load trained model
model = joblib.load( r"E:\OneDrive\Desktop\Customer Retention Analysis\models\rfm_churn_model.pkl")


@app.get("/")
def home():
    return {"message": "Customer Retention Analysis API is running!"}

@app.post("/predict_churn")
async def predict_churn(data: dict):
    # Convert incoming JSON data to DataFrame
    df = pd.DataFrame([data])

    # Print to check column names before prediction
    print("Received Data Format:", df.head())  # Debugging step

    # Ensure correct feature names
    df = df[['recency', 'frequency', 'monetary']]

    # Predict churn probability
    proba_output = model.predict_proba(df)

    return {"churn_probability": proba_output[:, 1].tolist()}

