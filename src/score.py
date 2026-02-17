import json
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def init():
    global model
    model_path = "random_forest.pkl"
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)
        df = pd.DataFrame([data])

        # Ensure correct column order
        expected_cols = ["Dur", "Proto_encoded", "SrcPort", "DstPort", "Packets", "Bytes"]
        df = df[expected_cols]

        prediction = model.predict(df)[0]
        label = "Attack" if prediction == 1 else "Normal"

        return {"prediction": int(prediction), "label": label}

    except Exception as e:
        return {"error": str(e)}
