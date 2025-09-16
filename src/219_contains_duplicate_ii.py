from typing import List

import pytest


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i, num in enumerate(nums):
            if num in map and i - map[num] <= k:
                return True
            map[num] = i

        return False


@pytest.mark.parametrize(
    ("nums", "k", "expected"),
    [([1, 2, 3, 1], 3, True), ([1, 0, 1, 1], 1, True), ([1, 2, 3, 1, 2, 3], 2, False)],
)
def test_containsNearbyDuplicate(nums: List[int], k: int, expected: bool):
    assert Solution().containsNearbyDuplicate(nums, k) == expected
