import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class YouTubeScraper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # UI 없이 실행
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def scrape_comments(self, url, max_comments=100):
        self.driver.get(url)
        time.sleep(3)

        # 스크롤 내려서 댓글 더 보기
        self.scroll_to_load(max_comments)

        # 댓글 추출
        comment_elements = self.driver.find_elements(By.CSS_SELECTOR, "#content-text")
        comments = [el.text for el in comment_elements if el.text.strip() != ""]

        self.driver.quit()
        return comments[:max_comments]

    def scroll_to_load(self, max_comments):
        last_height = self.driver.execute_script("return document.documentElement.scrollHeight")
        count = 0

        while count < max_comments:
            self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            count += 10 
    def close(self):
        self.driver.quit()


if __name__ == "__main__":
    url = "https://youtu.be/dQw4w9WgXcQ"
    scraper = YouTubeScraper()
    comments = scraper.scrape_comments(url, max_comments=20)
    for c in comments:
        print(c)
