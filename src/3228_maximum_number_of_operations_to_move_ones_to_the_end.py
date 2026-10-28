import pytest


class Solution:
    def maxOperations(self, s: str) -> int:
        num_of_ones = 0
        ops = 0

        # any time we encounter 1 followed by 0,
        # it means we can bubble all the 1s we've encountered so far
        for i in range(len(s) - 1):
            if s[i] == "1":
                num_of_ones += 1

                if s[i + 1] == "0":
                    ops += num_of_ones

        return ops


@pytest.mark.parametrize(("s", "expected"), [("1001101", 4), ("00111", 0)])
def test_maxOperations(s: str, expected: int):
    assert Solution().maxOperations(s) == expected
