from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils.yt_scraper import YouTubeScraper
import joblib

app = FastAPI()

SWEAR_MODEL_PATH = "models/swear_detector.pkl"
AD_MODEL_PATH = "models/ad_detector.pkl"

swear_model = joblib.load(SWEAR_MODEL_PATH)
ad_model = joblib.load(AD_MODEL_PATH)

class URLRequest(BaseModel):
    url: str
    max: int = 100

@app.post("/analyze-comments")
def analyze_comments(request: URLRequest):
    scraper = YouTubeScraper()
    try:
        comments = scraper.scrape_comments(request.url, max_comments=request.max)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"크롤링 실패: {str(e)}")
    finally:
        scraper.close()

    swear_preds = swear_model.predict(comments)
    ad_preds = ad_model.predict(comments)

    results = []
    for comment, s_pred, a_pred in zip(comments, swear_preds, ad_preds):
        results.append({
            "comment": comment,
            "욕설": bool(s_pred),
            "광고": bool(a_pred)
        })

    return {
        "count": len(results),
        "results": results
    }
