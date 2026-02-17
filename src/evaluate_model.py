import pandas as pd
import joblib
from sklearn.metrics import classification_report, roc_auc_score

def evaluate(model_path, data_path):
    model = joblib.load(model_path)
    df = pd.read_csv(data_path)

    X = df.drop(columns=['Label_encoded'])
    y = df['Label_encoded']

    preds = model.predict(X)
    print(classification_report(y, preds))

    try:
        auc = roc_auc_score(y, preds)
        print("AU-ROC:", auc)
    except:
        print("AU-ROC could not be computed.")

if __name__ == "__main__":
    evaluate("models/random_forest.pkl", "data/processed/sample_processed.csv")
