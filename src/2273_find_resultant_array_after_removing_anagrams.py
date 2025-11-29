from typing import List

import pytest


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def char_counts(word: str) -> List[int]:
            counts = [0] * 26
            for c in word:
                counts[ord(c) - ord("a")] += 1
            return counts

        i = len(words) - 1
        while i > 0:
            if char_counts(words[i]) == char_counts(words[i - 1]):
                words.pop(i)

            i -= 1

        return words


@pytest.mark.parametrize(
    ("words", "expected"),
    [
        (["abba", "baba", "bbaa", "cd", "cd"], ["abba", "cd"]),
        (["a", "b", "c", "d", "e"], ["a", "b", "c", "d", "e"]),
    ],
)
def test_removeAnagrams(words: List[str], expected: List[str]):
    assert Solution().removeAnagrams(words) == expected
