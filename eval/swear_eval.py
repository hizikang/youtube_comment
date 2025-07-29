import json
import joblib
from sklearn.metrics import classification_report

MODEL_PATH = "models/swear_detector.pkl"
TEST_PATH = "data/swear_eval.json"

model = joblib.load(MODEL_PATH)

with open(TEST_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

texts = [item["text"] for item in data]
labels = [item["label"] for item in data]

preds = model.predict(texts)

print("\n[ 현실 댓글 테스트셋 평가 결과 ]")
print(classification_report(labels, preds, target_names=["비욕설", "욕설"]))
