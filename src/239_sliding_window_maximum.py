from collections import deque
from typing import List

import pytest


# monotonic queue: queue[0] is always max
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        queue = deque()
        for i in range(len(nums)):
            if i < k - 1:
                while queue and nums[queue[-1]] < nums[i]:
                    queue.pop()
                queue.append(i)
            else:
                # slide window
                if queue and queue[0] == i - k:
                    queue.popleft()
                while queue and nums[queue[-1]] < nums[i]:
                    queue.pop()
                queue.append(i)

                result.append(nums[queue[0]])

        return result


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]), ([1], 1, [1])],
)
def test_maxSlidingWindow(nums: List[int], k: int, expected: int):
    assert Solution().maxSlidingWindow(nums, k) == expected
