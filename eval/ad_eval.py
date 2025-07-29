import json
import joblib
from sklearn.metrics import classification_report

TEST_PATH = "data/ad_eval.json"
MODEL_PATH = "models/ad_detector.pkl"

with open(TEST_PATH, "r", encoding="utf-8") as f:
    test_data = json.load(f)

texts = [item["text"] for item in test_data]
labels = [item["label"] for item in test_data]

model = joblib.load(MODEL_PATH)
predictions = model.predict(texts)

print("[ 광고 분류 모델 평가 ]")
print(classification_report(labels, predictions, target_names=["비광고", "광고"]))
