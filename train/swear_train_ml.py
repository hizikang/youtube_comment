import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# 경로 설정
DATA_PATH = "data/swear_train.json"
MODEL_PATH = "model/swear_detector.pkl"

# 데이터 로드
with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

texts = [item["text"] for item in data]
labels = [item["label"] for item in data]

# 파이프라인 구성 (TF-IDF + 로지스틱 회귀)
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression(solver="liblinear")),
])

# 전체 데이터로 학습
pipeline.fit(texts, labels)

# 모델 저장
os.makedirs("model", exist_ok=True)
joblib.dump(pipeline, MODEL_PATH)
print(f"최종 모델 저장 완료 → {MODEL_PATH}")