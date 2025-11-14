from typing import Set

import pytest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        max_length_str = ""

        for i in range(len(s)):
            # odd length
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left - 1
            if length > max_length:
                max_length = length
                max_length_str = s[left + 1 : right]

            # even length
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            length = right - left - 1
            if length > max_length:
                max_length = length
                max_length_str = s[left + 1 : right]

        return max_length_str


@pytest.mark.parametrize(
    ("s", "expected"), [("babad", {"bab", "aba"}), ("cbbd", {"bb"})]
)
def test_longestPalindrome(s: str, expected: Set[str]):
    assert Solution().longestPalindrome(s) in expected
