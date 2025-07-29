import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
import joblib

# 경로 설정
DATA_PATH = "data/swear_train.json"
MODEL_PATH = "models/swear_detector.pkl"

# 데이터 로드
with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

texts = [item["text"] for item in data]
labels = [item["label"] for item in data]

# TF-IDF + XGBoost 분류기 파이프라인
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", XGBClassifier(
        n_estimators=100,
        max_depth=4,
        learning_rate=0.1,
        use_label_encoder=False,
        eval_metric="logloss",
        verbosity=0
    )),
])

# 모델 학습
pipeline.fit(texts, labels)

# 저장 디렉토리 생성 및 모델 저장
os.makedirs("models", exist_ok=True)
joblib.dump(pipeline, MODEL_PATH)
print(f"최종 모델 저장 완료 → {MODEL_PATH}")
