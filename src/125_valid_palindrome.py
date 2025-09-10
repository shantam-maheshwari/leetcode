import pytest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if not s[left].lower() == s[right].lower():
                return False

            left += 1
            right -= 1

        return True


@pytest.mark.parametrize(
    ("s", "expected"),
    [("A man, a plan, a canal: Panama", True), ("race a car", False), (" ", True)],
)
def test_isPalindrome(s: str, expected: bool):
    assert Solution().isPalindrome(s) == expected
