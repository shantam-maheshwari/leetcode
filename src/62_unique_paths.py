import pytest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1] * n

        for i in range(1, m):
            curr = [0] * n
            curr[0] = 1

            for j in range(1, n):
                curr[j] = curr[j - 1] + prev[j]

            prev = curr

        return prev[n - 1]


@pytest.mark.parametrize(("m", "n", "expected"), [(3, 7, 28), (3, 2, 3)])
def test_uniquePaths(m: int, n: int, expected: int):
    assert Solution().uniquePaths(m, n) == expected
