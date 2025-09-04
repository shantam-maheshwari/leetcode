from typing import List

import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in visited:
                return [i, visited[diff]]
            visited[num] = i

        return [-1, -1]


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [([2, 7, 11, 15], 9, [0, 1]), ([3, 2, 4], 6, [1, 2]), ([3, 3], 6, [0, 1])],
)
def test_twoSum(nums: List[int], target: int, expected: List[int]):
    assert sorted(Solution().twoSum(nums, target)) == sorted(expected)
