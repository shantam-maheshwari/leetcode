import pytest

# # time: O(len(s1) * len(s2)), space: O(len(s1) * len(s2))
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         if not text1 or not text2:
#             return 0

#         dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

#         for i1 in range(1, len(text1) + 1):
#             for i2 in range(1, len(text2) + 1):
#                 if text1[i1 - 1] == text2[i2 - 1]:
#                     dp[i1][i2] = dp[i1 - 1][i2 - 1] + 1
#                 else:
#                     dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])

#         return dp[-1][-1]


# time: O(len(s1) * len(s2)), space: O(min(len(s1), len(s2)))
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        prev = [0] * (len(text2) + 1)

        for i1 in range(1, len(text1) + 1):
            curr = [0] * (len(text2) + 1)
            for i2 in range(1, len(text2) + 1):
                if text1[i1 - 1] == text2[i2 - 1]:
                    curr[i2] = prev[i2 - 1] + 1
                else:
                    curr[i2] = max(prev[i2], curr[i2 - 1])
            prev = curr

        return prev[-1]


@pytest.mark.parametrize(
    ("text1", "text2", "expected"),
    [("abcde", "ace", 3), ("abc", "abc", 3), ("abc", "def", 0)],
)
def test_longestCommonSubsequence(text1: str, text2: str, expected: str):
    assert Solution().longestCommonSubsequence(text1, text2) == expected
