from typing import List

import pytest


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_length = 0

        left = 0
        right = 0
        zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
    ],
)
def test_longestOnes(nums: List[int], k: int, expected: int):
    assert Solution().longestOnes(nums, k) == expected
