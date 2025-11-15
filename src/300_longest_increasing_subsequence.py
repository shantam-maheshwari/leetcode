from typing import List

import pytest


# dp
# time: O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# TODO: there exists a O(nlog(n)) solution as well using binary search


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ],
)
def test_lengthOfLIS(nums: List[int], expected: int):
    assert Solution().lengthOfLIS(nums) == expected
