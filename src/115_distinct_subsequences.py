import pytest


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] = how many subsequences in s[:i] exactly match t[:j]
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        for i in range(len(s) + 1):
            dp[i][0] = 1

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[-1][-1]


@pytest.mark.parametrize(
    ("s", "t", "expected"), [("rabbbit", "rabbit", 3), ("babgbag", "bag", 5)]
)
def test_numDistinct(s: str, t: str, expected: int):
    assert Solution().numDistinct(s, t) == expected
