import pytest
from filter.swear_comment import predict_swear

@pytest.mark.parametrize("text, expected", [
    ("씨발 오늘 진짜 짜증난다", 1),
    ("감사합니다 좋은 하루 되세요", 0),
    ("야이 개새끼야", 1),
    ("이 영상 너무 유익하네요", 0),
    ("좆같은 상황", 1),
    ("개쩐다 진짜", 0),
])
def test_predict_swear(text, expected):
    assert predict_swear(text) == expected, f"Failed on: {text}"
