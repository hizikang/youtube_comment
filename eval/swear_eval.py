import json
import joblib
from sklearn.metrics import classification_report

MODEL_PATH = "model/swear_detector.pkl"
TEST_PATH = "data/swear_eval.json"

# 모델 로드
model = joblib.load(MODEL_PATH)

# 테스트셋 로드
with open(TEST_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

texts = [item["text"] for item in data]
labels = [item["label"] for item in data]

# 예측 및 평가
preds = model.predict(texts)

print("\n[ 현실 댓글 테스트셋 평가 결과 ]")
print(classification_report(labels, preds, target_names=["비욕설", "욕설"]))
