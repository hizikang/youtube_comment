import json
import os
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

DATA_PATH = "data/ad_train.json"
MODEL_PATH = "models/ad_detector.pkl"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

texts = [item["text"] for item in data]
labels = [item["label"] for item in data]

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(solver="liblinear"))
])

pipeline.fit(texts, labels)

os.makedirs("models", exist_ok=True)
joblib.dump(pipeline, MODEL_PATH)
print(f"최종 모델 저장 완료 → {MODEL_PATH}")
