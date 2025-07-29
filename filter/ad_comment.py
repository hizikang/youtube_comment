import joblib
import os

MODEL_PATH = "models/ad_detector.pkl"
model = joblib.load(MODEL_PATH)

def predict_ad(text: str) -> int:
    return int(model.predict([text])[0])
