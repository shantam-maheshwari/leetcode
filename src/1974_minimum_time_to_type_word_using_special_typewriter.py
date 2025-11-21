import pytest


class Solution:
    def minTimeToType(self, word: str) -> int:
        result = len(word)
        curr = "a"
        for i in range(len(word)):
            clockwise = abs(ord(word[i]) - ord(curr))
            anti_clockwise = 26 - clockwise
            result += min(clockwise, anti_clockwise)
            curr = word[i]
        return result


@pytest.mark.parametrize(("word", "expected"), [("abc", 5), ("bza", 7), ("zjpc", 34)])
def test_minTimeToType(word: str, expected: int):
    assert Solution().minTimeToType(word) == expected
