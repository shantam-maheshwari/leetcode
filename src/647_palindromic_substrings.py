import pytest


class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            # odd length
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1

            # even length
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1

        return result


@pytest.mark.parametrize(("s", "expected"), [("abc", 3), ("aaa", 6), ("aaaa", 10)])
def test_countSubstrings(s: str, expected: int):
    assert Solution().countSubstrings(s) == expected
