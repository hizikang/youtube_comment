# YouTube 댓글 필터링 자동화 시스템
### 25.07 ~ (개인프로젝트)

## 1. 개요

본 프로젝트는 유튜브 영상의 댓글을 자동으로 수집하고, 수집된 댓글에서 **욕설 및 광고성 댓글을 필터링**하는 QA 자동화 파이프라인
Selenium 기반의 웹 크롤링, 정규표현식 및 금치어 기본 필터링 로직, 평가용 테스트센 및 자동화된 필터 정확도 검사 기능을 포함

---

## 2. 프로젝트 구조 (Project Structure)

```
youtube_comment/
├── main.py                    
├── data/
│   ├── comments.json          # 원본 댓글 데이터
│   └── comments_filtered.json # 필터링된 댓글 결과
├── utils/
│   └── yt_scraper.py          # Selenium 기반 댓글 크롤링
├── filter/
│   ├── comment_filter.py      # 욕설/광고 필터링 로직
│   └── evaluate_filter.py     # 필터 정확도 검사 스크립트 
├── tests/
│   └── test_filtering.py      # pytest 기반 테스트
├── requirements.txt           
└── README.md                  
```

---

## 3. 주요 기능

| 기능          | 설명                                      |
| ----------- | --------------------------------------- |
| 댓글 수집     | YouTube URL을 입력받아 댓글 크롤링 (Selenium 기반)  |
| 욕설 필터링    | 정규표현식 및 금치어 리스트 기본 요설 필터링               |
| 광고 필터링    | 링크/템레그램/오픈채팅 등 키워드 기본 광고 탐지             |
| 결과 저장     | 필터링 결과를 JSON 파일로 저장 (`is_bad`, `is_ad`) |
| 유니트 테스트   | 각 필터 로직에 대한 pytest 기반 테스트 포함            |
| 필터 정확도 검사 | 라벨링된 정답센과 비교하여 precision/recall 계산      |

---

## 4. 사용 기술 

* **Python 3.10+**
* **Selenium**: YouTube 댓글 크롤링 자동화
* **Regex**: 욕설 및 광고 탐지 패턴 정의
* **Pytest**: 테스트 및 QA 자동화
* **JSON**: 데이터 입출력 및 저장
* **FastAPI** : API

---

## 5. 실행 방법 

```bash
# 필요 패키지 설치
pip install -r requirements.txt

# 유튜브 영상 댓글 수집 및 필터링 실행
python main.py --url "https://youtu.be/ICc20UBLb-Q" --max 150
```

실행 결과:

* `data/comments.json`: 원본 댓글 목록
* `data/comments_filtered.json`: 필터링 결과

  ```json
  {
    "comment": "씨발 무엉 이것",
    "is_bad": true,
    "is_ad": false
  }
  ```

---

## 6. 필터 정확도 검사

```bash
python filter/evaluate_filter.py
```

* 정답(`truth.json`)과 필터 결과 비교
* 요설/광고 탐지의 **Precision / Recall / F1-score** 출력

---

## 7. 테스트 실행 (Unit Tests)

```bash
pytest tests/
```

* 욕설/광고 필터 로직에 대한 단위 테스트 수행

```bash
pytest --cov=filter
```

---

## 8. 피부 개정 사항 (To-do / Ideas)

* [ ] **욕설 변형 탐지 강화** (ex. `ㅅㅂ`, `ㅅ ㅂ`, `fuckkk`)
* [ ] **자연어 기본 분류기 도입**
* [ ] **실시간 댓글 모니터링 API 연동**

---

## 9. 역할

* Selenium 기반 크롤링 로직 구현
* 요설/광고 필터링 로직 정의 및 테스트센 구축
* 필터 정확도 검사 로직 설계
* 전체 실행 파이프라인 구성 및 예외 처리/로그 추가