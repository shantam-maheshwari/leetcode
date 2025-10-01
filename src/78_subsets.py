from typing import List

import pytest


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack([], 0, nums, result)
        return result

    def backtrack(
        self, candidate: List[int], i: int, nums: List[int], result: List[List[int]]
    ):
        if i == len(nums):
            result.append(candidate.copy())
            return

        self.backtrack(candidate, i + 1, nums, result)

        candidate.append(nums[i])
        self.backtrack(candidate, i + 1, nums, result)
        candidate.pop()


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
    ],
)
def test_subsets(nums: List[int], expected: List[List[int]]):
    result = [tuple(x) for x in Solution().subsets(nums)]
    expected = [tuple(x) for x in expected]
    assert set(result) == set(expected)
