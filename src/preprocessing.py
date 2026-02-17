import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df = df.dropna()
    return df

def encode_features(df):
    le = LabelEncoder()
    if 'Proto' in df.columns:
        df['Proto_encoded'] = le.fit_transform(df['Proto'])
        df = df.drop(columns=['Proto'])
    return df

def normalize(df):
    scaler = MinMaxScaler()
    numeric_cols = df.select_dtypes(include=['int64','float64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
    return df

def save_processed(df, path):
    df.to_csv(path, index=False)
