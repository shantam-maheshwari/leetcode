from typing import List

import pytest

# # prefix sums, space: O(n)
# class Solution:
#     def waysToSplitArray(self, nums: List[int]) -> int:
#         prefix_sums = [0] * len(nums)
#         curr_sum = 0
#         for i, num in enumerate(nums):
#             curr_sum += num
#             prefix_sums[i] = curr_sum

#         result = 0
#         for i in range(len(nums) - 1):
#             if prefix_sums[i] >= curr_sum - prefix_sums[i]:
#                 result += 1

#         return result


# prefix sums, space: O(1)
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        result = 0

        total = sum(nums)
        left_sum = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total - left_sum
            if left_sum >= right_sum:
                result += 1

        return result


@pytest.mark.parametrize(("nums", "expected"), [([10, 4, -8, 7], 2), ([2, 3, 1, 0], 2)])
def test_waysToSplitArray(nums: List[int], expected: int):
    assert Solution().waysToSplitArray(nums) == expected
