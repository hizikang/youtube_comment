from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class YouTubeScraper:
    def __init__(self, headless: bool = True):
        options = Options()
        if headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--lang=ko-KR")
        self.driver = webdriver.Chrome(options=options)

    def scrape(self, video_url: str, max_count: int = 100) -> list:
        self.driver.get(video_url)
        time.sleep(3)
        last_height = self.driver.execute_script("return document.documentElement.scrollHeight")
        comments = []
        while len(comments) < max_count:
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            els = self.driver.find_elements(By.XPATH, '//*[@id="content-text"]')
            texts = [e.text.strip() for e in els if e.text.strip()]
            comments = list(dict.fromkeys(comments + texts))
        return comments[:max_count]

    def close(self):
        self.driver.quit()