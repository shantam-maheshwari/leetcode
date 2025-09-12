from typing import List

import pytest


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i1 = m - 1
        i2 = n - 1
        j = m + n - 1
        while i2 >= 0:
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[j] = nums1[i1]
                i1 -= 1
            else:
                nums1[j] = nums2[i2]
                i2 -= 1

            j -= 1


@pytest.mark.parametrize(
    ("nums1", "m", "nums2", "n", "expected"),
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ],
)
def test_merge(nums1: List[int], m: int, nums2: List[int], n: int, expected: List[int]):
    Solution().merge(nums1, m, nums2, n)
    assert nums1 == expected
