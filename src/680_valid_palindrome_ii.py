import pytest


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                result = self.is_palindrome(s, left + 1, right) or self.is_palindrome(
                    s, left, right - 1
                )
                return result
        return True

    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


@pytest.mark.parametrize(
    ("s", "expected"), [("aba", True), ("abc", False), ("abbxa", True)]
)
def test_validPalindrome(s: str, expected: bool):
    assert Solution().validPalindrome(s) == expected
