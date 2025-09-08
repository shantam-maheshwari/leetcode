from typing import List

import pytest


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        first = self.binary_search_left(0, len(nums) - 1, nums, target)

        if first == -1:
            return [-1, -1]

        last = self.binary_search_right(first, len(nums) - 1, nums, target)
        return [first, last]

    def binary_search_left(
        self, left: int, right: int, nums: List[int], target: int
    ) -> int:
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left if nums[left] == target else -1

    def binary_search_right(
        self, left: int, right: int, nums: List[int], target: int
    ) -> int:
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        return left if nums[left] == target else -1


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
    ],
)
def test_searchRange(nums: List[int], target: int, expected: List[int]):
    assert Solution().searchRange(nums, target) == expected
