from typing import List

import pytest


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        # find building that don't have an equal or higher building to the right
        result = []
        tallest_so_far = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > tallest_so_far:
                result.append(i)
                tallest_so_far = heights[i]
        result.reverse()
        return result


@pytest.mark.parametrize(
    ("heights", "expected"),
    [([4, 2, 3, 1], [0, 2, 3]), ([4, 3, 2, 1], [0, 1, 2, 3]), ([1, 3, 2, 4], [3])],
)
def test_findBuildings(heights: List[int], expected: List[int]):
    assert Solution().findBuildings(heights) == expected
