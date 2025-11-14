from typing import List

import pytest


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        result = set()

        def generateSubarrays(nums: List[int]):
            for i in range(len(nums)):
                result.add(tuple(nums[i:]))

        left = right = 0
        while right < len(nums):
            if nums[right] % p == 0:
                k -= 1

            while k < 0:
                if nums[left] % p == 0:
                    k += 1
                left += 1

            generateSubarrays(nums[left : right + 1])
            right += 1

        return len(result)


@pytest.mark.parametrize(
    ("nums", "k", "p", "expected"),
    [([2, 3, 3, 2, 2], 2, 2, 11), ([1, 2, 3, 4], 4, 1, 10)],
)
def test_countDistinct(nums: List[int], k: int, p: int, expected: int):
    assert Solution().countDistinct(nums, k, p) == expected
