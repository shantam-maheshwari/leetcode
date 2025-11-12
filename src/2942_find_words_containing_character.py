from typing import List

import pytest


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if word.find(x) != -1]


@pytest.mark.parametrize(
    ("words", "x", "expected"),
    [
        (["leet", "code"], "e", [0, 1]),
        (["abc", "bcd", "aaaa", "cbc"], "a", [0, 2]),
        (["abc", "bcd", "aaaa", "cbc"], "z", []),
    ],
)
def test_findWordsContaining(words: List[str], x: str, expected: List[int]):
    assert Solution().findWordsContaining(words, x) == expected
