from typing import List

import pytest


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        pivot = len(nums) - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        if pivot == -1:
            nums.reverse()
            return

        right = len(nums) - 1
        while nums[right] <= nums[pivot]:
            right -= 1

        nums[pivot], nums[right] = nums[right], nums[pivot]
        nums[pivot + 1 :] = reversed(nums[pivot + 1 :])


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([], []),
        ([1, 2, 3, 4], [1, 2, 4, 3]),
        ([3, 4, 2, 1], [4, 1, 2, 3]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
    ],
)
def test_nextPermutation(nums: List[int], expected: List[int]):
    Solution().nextPermutation(nums)
    assert nums == expected
