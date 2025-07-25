from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import json
import os

def crawl_youtube_comments(video_url: str, output_path: str = "data/comments.json", max_count: int = 100):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=ko-KR")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(video_url)
    time.sleep(3)

    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    comments = []
    while len(comments) < max_count:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        els = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
        texts = [e.text.strip() for e in els if e.text.strip()]
        comments = list(dict.fromkeys(comments + texts))

    driver.quit()

    os.makedirs("data", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(comments[:max_count], f, ensure_ascii=False, indent=2)

    print(f"댓글 {len(comments)}개 저장 완료 → {output_path}")