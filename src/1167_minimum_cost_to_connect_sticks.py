import heapq
from typing import List

import pytest


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = sticks
        heapq.heapify(sticks)

        cost = 0
        while len(heap) > 1:
            new_stick = heapq.heappop(heap) + heapq.heappop(heap)
            cost += new_stick
            heapq.heappush(heap, new_stick)
        return cost


@pytest.mark.parametrize(("sticks", "expected"), [([2, 4, 3], 14), ([1, 8, 3, 5], 30)])
def test_connectSticks(sticks: List[int], expected: int):
    assert Solution().connectSticks(sticks) == expected
