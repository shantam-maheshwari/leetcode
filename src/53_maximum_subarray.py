from typing import List

import pytest


class Solution:
    # # space complexity: O(n)
    # def maxSubArray(self, nums: List[int]) -> int:
    #     n = len(nums)

    #     if n == 0:
    #         return 0

    #     memo = [float("-inf")] * n
    #     memo[0] = max_sum = nums[0]

    #     for i in range(1, n):
    #         memo[i] = max(memo[i - 1] + nums[i], nums[i])
    #         max_sum = max(max_sum, memo[i])

    #     return max_sum

    # space complexity: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        curr_sum = max_sum = nums[0]
        for i in range(1, n):
            curr_sum = max(curr_sum + nums[i], nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum


@pytest.mark.parametrize(
    ("nums", "expected"),
    [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6), ([1], 1), ([5, 4, -1, 7, 8], 23)],
)
def test_maxSubArray(nums: List[int], expected: int):
    assert Solution().maxSubArray(nums) == expected
