import heapq
from typing import List

import pytest


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for [x, y] in points:
            distance_squared = x * x + y * y
            heapq.heappush(heap, (-distance_squared, [x, y]))

            if len(heap) > k:
                heapq.heappop(heap)

        return [p[1] for p in heap]


@pytest.mark.parametrize(
    ("points", "k", "expected"),
    [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
    ],
)
def test_kClosest(points: List[List[int]], k: int, expected: List[List[int]]):
    result = [tuple(p) for p in Solution().kClosest(points, k)]
    expected = [tuple(p) for p in expected]
    assert set(result) == set(expected)
