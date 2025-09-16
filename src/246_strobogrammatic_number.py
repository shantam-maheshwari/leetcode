import pytest


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pairs = {("0", "0"), ("1", "1"), ("8", "8"), ("6", "9"), ("9", "6")}
        left = 0
        right = len(num) - 1
        while left <= right:
            if (num[left], num[right]) not in pairs:
                return False
            left += 1
            right -= 1
        return True


@pytest.mark.parametrize(
    ("num", "expected"),
    [("69", True), ("88", True), ("962", False), ("2", False), ("1", True)],
)
def test_isStrobogrammatic(num: str, expected: int):
    assert Solution().isStrobogrammatic(num) == expected
