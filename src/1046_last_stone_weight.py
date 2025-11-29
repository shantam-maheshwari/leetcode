import heapq
from typing import List

import pytest


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            if stone1 == stone2:
                continue

            heapq.heappush(heap, -abs(stone1 - stone2))

        return -heapq.heappop(heap) if heap else 0


@pytest.mark.parametrize(("stones", "expected"), [([2, 7, 4, 1, 8, 1], 1), ([1], 1)])
def test_lastStoneWeight(stones: List[int], expected: int):
    assert Solution().lastStoneWeight(stones) == expected
