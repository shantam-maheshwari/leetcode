from typing import List

import pytest


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        left = 0
        right = len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


@pytest.mark.parametrize(
    ("height", "expected"), [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49), ([1, 1], 1)]
)
def test_maxArea(height: List[int], expected: int):
    assert Solution().maxArea(height) == expected
