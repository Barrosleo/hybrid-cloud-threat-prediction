import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(data_path, model_path):
    df = pd.read_csv(data_path)
    X = df.drop(columns=['Label_encoded'])
    y = df['Label_encoded']

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    joblib.dump(model, model_path)
    print("Model saved:", model_path)

if __name__ == "__main__":
    train_model("data/processed/sample_processed.csv", "models/random_forest.pkl")
