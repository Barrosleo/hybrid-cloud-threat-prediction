import os
from src.train_model import train_model

def test_train_model():
    train_model("data/processed/sample_processed.csv", "models/test_model.pkl")
    assert os.path.exists("models/test_model.pkl")
    os.remove("models/test_model.pkl")
