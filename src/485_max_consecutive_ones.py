from typing import List

import pytest


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0

        for num in nums:
            if num == 0:
                count = 0
            else:
                count += 1
                max_count = max(max_count, count)

        return max_count


@pytest.mark.parametrize(
    ("nums", "expected"), [([1, 1, 0, 1, 1, 1], 3), ([1, 0, 1, 1, 0, 1], 2)]
)
def test_findMaxConsecutiveOnes(nums: List[int], expected: int):
    assert Solution().findMaxConsecutiveOnes(nums) == expected
