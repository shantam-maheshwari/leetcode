from typing import List

import pytest


# https://leetcode.com/discuss/post/7313940/jpmc-jp-morgon-cohort-hiring-swe-3-rejec-p5fy/
class Solution:
    def flipSigns(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        Given an array nums and a list of queries, where each query is [L, R],
        flip the sign of every element nums[i] for L <= i <= R.

        Return the final array after processing all queries.
        """

        flip_signs = [False] * (len(nums) + 1)
        for [L, R] in queries:
            flip_signs[L] = not flip_signs[L]
            flip_signs[R + 1] = not flip_signs[R + 1]

        flip = False
        for i in range(len(nums)):
            flip ^= flip_signs[i]
            if flip:
                nums[i] = -nums[i]

        return nums


@pytest.mark.parametrize(
    ("nums", "queries", "expected"),
    [([5, -1, 3, 7, -4, 2], [[1, 3], [2, 5], [0, 0]], [-5, 1, 3, 7, 4, -2])],
)
def test_flipSigns(nums: List[int], queries: List[List[int]], expected: List[int]):
    assert Solution().flipSigns(nums, queries) == expected
