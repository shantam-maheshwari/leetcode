import heapq
from typing import List

import pytest


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap)


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [([3, 2, 1, 5, 6, 4], 2, 5), ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)],
)
def test_findKthLargest(nums: List[int], k: int, expected: int):
    assert Solution().findKthLargest(nums, k) == expected
