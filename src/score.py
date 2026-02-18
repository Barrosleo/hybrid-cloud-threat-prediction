from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# Load model at startup
model = joblib.load("models/random_forest.pkl")

@app.get("/")
def home():
    return {"message": "Hybrid Cloud Threat Prediction API is running"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    label = "Attack" if prediction == 1 else "Normal"
    return {"prediction": int(prediction), "label": label}

