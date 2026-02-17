import pandas as pd
from src.preprocessing import clean_data, encode_features

def test_clean_data():
    df = pd.DataFrame({"A": [1, None]})
    cleaned = clean_data(df)
    assert cleaned.shape[0] == 1

def test_encode_features():
    df = pd.DataFrame({"Proto": ["tcp", "udp"]})
    encoded = encode_features(df)
    assert "Proto_encoded" in encoded.columns
