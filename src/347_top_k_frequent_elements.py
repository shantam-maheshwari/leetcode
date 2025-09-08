import heapq
from typing import Counter, List

import pytest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        heap = []
        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [pair[1] for pair in heap]


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2, [1, 2]),
    ],
)
def test_topKFrequent(nums: List[int], k: int, expected: List[int]):
    assert set(Solution().topKFrequent(nums, k)) == set(expected)
