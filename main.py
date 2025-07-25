import argparse
from utils.yt_scraper import YouTubeScraper
from filter.comment_filter import filter_comments
import os, json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube 댓글 QA 파이프라인")
    parser.add_argument("--url", required=True, help="크롤링할 YouTube 영상 URL")
    parser.add_argument("--max", type=int, default=100, help="최대 크롤링 댓글 수")
    args = parser.parse_args()

    scraper = YouTubeScraper()
    comments = scraper.scrape(args.url, max_count=args.max)
    scraper.close()

    os.makedirs("data", exist_ok=True)
    with open("data/comments.json", "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)
    print(f"comments.json에 {len(comments)}개 저장됨")

    filter_comments("data/comments.json")
