import json
import re

BAD_WORDS = [
    "씨발", "ㅅㅂ", "병신", "개새끼",
    "fuck", "shit", "좆", "ㅈㄹ"
]

AD_PATTERNS = [
    r"http[s]?://", r"www\\.", r"카카오톡", r"텔레그램", r"오픈채팅", r"문의"
]

def is_bad_comment(text: str) -> bool:
    t = text.lower()
    return any(word in t for word in BAD_WORDS)

def is_ad_comment(text: str) -> bool:
    return any(re.search(pat, text, re.IGNORECASE) for pat in AD_PATTERNS)

def filter_comments(input_path: str = "data/comments.json") -> None:
    with open(input_path, "r", encoding="utf-8") as f:
        comments = json.load(f)

    results = []
    for c in comments:
        results.append({
            "comment": c,
            "is_bad": is_bad_comment(c),
            "is_ad": is_ad_comment(c)
        })

    output_path = input_path.replace(".json", "_filtered.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"필터링 완료 → {output_path}")