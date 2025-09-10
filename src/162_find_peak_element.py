from typing import List

import pytest


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


@pytest.mark.parametrize(
    ("nums", "expected"), [([1, 2, 3, 1], [2]), ([1, 2, 1, 3, 5, 6, 4], [1, 5])]
)
def test_findPeakElement(nums: List[int], expected: List[int]):
    assert Solution().findPeakElement(nums) in set(expected)
