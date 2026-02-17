from src.preprocessing import load_data, clean_data, encode_features, normalize, save_processed
from src.train_model import train_model
from src.evaluate_model import evaluate

RAW_PATH = "data/raw/sample_raw.csv"
PROCESSED_PATH = "data/processed/sample_processed.csv"
MODEL_PATH = "models/random_forest.pkl"

def main():
    print("Loading data...")
    df = load_data(RAW_PATH)

    print("Cleaning data...")
    df = clean_data(df)

    print("Encoding features...")
    df = encode_features(df)

    print("Normalizing...")
    df = normalize(df)

    print("Saving processed data...")
    save_processed(df, PROCESSED_PATH)

    print("Training model...")
    train_model(PROCESSED_PATH, MODEL_PATH)

    print("Evaluating model...")
    evaluate(MODEL_PATH, PROCESSED_PATH)

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
