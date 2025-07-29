from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils.yt_scraper import YouTubeScraper
import joblib
import os

app = FastAPI()
MODEL_PATH = "models/swear_detector.pkl"
model = joblib.load(MODEL_PATH)

class URLRequest(BaseModel):
    url: str
    max: int = 100

@app.post("/analyze-comments")
def analyze_comments(request: URLRequest):
    scraper = YouTubeScraper()
    try:
        comments = scraper.scrape_comments(request.url, request.max)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"크롤링 실패: {str(e)}")
    finally:
        scraper.close()

    predictions = model.predict(comments)
    results = [
        {
            "comment": c,
            "prediction": int(p),
            "label": "욕설" if p == 1 else "비욕설"
        } for c, p in zip(comments, predictions)
    ]

    return {
        "count": len(results),
        "results": results
    }
