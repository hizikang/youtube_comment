import joblib
import os

MODEL_PATH = "models/swear_detector.pkl"

_model = None
def load_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_swear(text: str) -> int:
    model = load_model()
    return model.predict([text])[0]
