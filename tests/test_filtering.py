import pytest
import json
from filter.comment_filter import is_bad_comment, is_ad_comment

@pytest.fixture(scope="module")
def sample_comments():
    return [
        "이 영상 씨발 대박!",
        "구독과 좋아요 부탁해요",
        "유익한 정보 감사합니다",
        "카카오톡 문의 주세요: chat123"
    ]

def test_is_bad_comment(sample_comments):
    assert is_bad_comment(sample_comments[0])
    assert not is_bad_comment(sample_comments[2])

def test_is_ad_comment(sample_comments):
    assert is_ad_comment(sample_comments[1])
    assert not is_ad_comment(sample_comments[2])