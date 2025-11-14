from typing import Dict

import pytest


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars_in_t = {}
        for c in t:
            chars_in_t[c] = chars_in_t.get(c, 0) + 1

        left = right = 0
        chars_in_window = {}
        min_start_idx = -1
        min_length = float("inf")

        while right < len(s):
            c = s[right]

            if c in chars_in_t:
                chars_in_window[c] = chars_in_window.get(c, 0) + 1

            while left <= right and isWindowValid(chars_in_window, chars_in_t):
                length = right - left + 1
                if length < min_length:
                    min_start_idx = left
                    min_length = length

                if s[left] in chars_in_window:
                    chars_in_window[s[left]] -= 1
                left += 1

            right += 1

        if min_start_idx == -1:
            return ""

        return s[min_start_idx : min_start_idx + min_length]


def isWindowValid(chars_in_window: Dict[str, int], chars_in_t: Dict[str, int]) -> bool:
    for c in chars_in_t:
        if c not in chars_in_window or chars_in_window[c] < chars_in_t[c]:
            return False
    return True


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [("ADOBECODEBANC", "ABC", "BANC"), ("a", "a", "a"), ("a", "aa", "")],
)
def test_minWindow(s: str, t: str, expected: str):
    assert Solution().minWindow(s, t) == expected
