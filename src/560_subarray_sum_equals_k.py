from typing import List

import pytest


class Solution:
    # # time: O(n^2), space: O(1)
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     result = 0
    #     for i in range(len(nums)):
    #         curr_sum = 0
    #         for j in range(i, len(nums)):
    #             curr_sum += nums[j]
    #             if curr_sum == k:
    #                 result += 1
    #     return result

    # time: O(n), space: O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        # we have to find number of 'a' and 'b' such that sum_a_to_b = k

        # sum_0_to_a + sum_a_to_b = curr_sum
        # => sum_0_to_a + k = curr_sum
        # => sum_0_to_a = curr_sum - k

        # at each 'b', we check if we've seen any 'a' such that sum_0_to_a = curr_sum - k

        result = 0

        prefix_sums = {}
        curr_sum = 0
        for num in nums:
            curr_sum += num

            if curr_sum == k:
                result += 1
            result += prefix_sums.get(curr_sum - k, 0)

            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        return result


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1, 3, 2, 4, 2], 6, 3),
        ([1], 0, 0),
        ([-1, -1, 1], 0, 1),
    ],
)
def test_subarraySum(nums: List[int], k: int, expected: int):
    assert Solution().subarraySum(nums, k) == expected
