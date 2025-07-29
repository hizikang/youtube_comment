import pytest
from filter.ad_comment import predict_ad

@pytest.mark.parametrize("text, expected", [
    ("지금 구매 시 특별 할인!", 1),
    ("다음 영상도 기대할게요!", 0),
    ("채널 홍보하러 왔습니다", 1),
    ("좋은 정보 감사합니다", 0),
])
def test_predict_ad(text, expected):
    assert predict_ad(text) == expected, f"Failed on: {text}"
