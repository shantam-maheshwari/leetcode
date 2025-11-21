from collections import defaultdict
from typing import List

import pytest

# # prefix sum counts (TLE)
# class Solution:
#     def subarraysDivByK(self, nums: List[int], k: int) -> int:
#         prefix_sums = defaultdict(int)
#         result = 0

#         curr_sum = 0
#         for i, num in enumerate(nums):
#             curr_sum += num
#             if curr_sum % k == 0:
#                 result += 1

#             for pre_sum in prefix_sums:
#                 if (curr_sum - pre_sum) % k == 0:
#                     result += prefix_sums[pre_sum]

#             prefix_sums[curr_sum] += 1
#         return result


# mod counts
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        curr_sum = 0
        mod_counts = defaultdict(int)
        mod_counts[0] = 1

        for num in nums:
            curr_sum += num
            mod = curr_sum % k
            result += mod_counts[mod]
            mod_counts[mod] += 1
        return result


@pytest.mark.parametrize(
    ("nums", "k", "expected"), [([4, 5, 0, -2, -3, 1], 5, 7), ([5], 9, 0)]
)
def test_subarraysDivByK(nums: List[int], k: int, expected: int):
    assert Solution().subarraysDivByK(nums, k) == expected
