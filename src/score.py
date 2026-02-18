from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(
    title="Hybrid Cloud Threat Prediction API",
    description="Machine Learning API for predicting cyber threats in hybrid cloud environments.",
    version="1.0.0"
)

# Load model at startup
model = joblib.load("models/random_forest.pkl")

@app.get("/")
def home():
    return {"message": "Hybrid Cloud Threat Prediction API is running"}

@app.post("/predict")
def predict(data: dict):
    """
    Accepts JSON input and returns a prediction.
    Example input:
    {
      "Dur": 0.12,
      "Proto_encoded": 1,
      "SrcPort": 443,
      "DstPort": 51514,
      "Packets": 10,
      "Bytes": 850
    }
    """
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    label = "Attack" if prediction == 1 else "Normal"
    return {"prediction": int(prediction), "label": label}
