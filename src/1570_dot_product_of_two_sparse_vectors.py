from typing import List

import pytest


class SparseVector:
    def __init__(self, nums: List[int]):
        self.vals = []
        for i, num in enumerate(nums):
            if num:
                self.vals.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        if not self.vals or not vec.vals:
            return 0

        result, i, j = 0, 0, 0
        while i < len(self.vals) and j < len(vec.vals):
            if self.vals[i][0] == vec.vals[j][0]:
                result += self.vals[i][1] * vec.vals[j][1]
                i += 1
                j += 1
            elif self.vals[i][0] < vec.vals[j][0]:
                i += 1
            else:
                j += 1
        return result


@pytest.mark.parametrize(
    ("nums1", "nums2", "expected"),
    [
        ([1, 0, 0, 2, 3], [0, 3, 0, 4, 0], 8),
        ([0, 1, 0, 0, 0], [0, 0, 0, 0, 2], 0),
        ([0, 1, 0, 0, 2, 0, 0], [1, 0, 0, 0, 3, 0, 4], 6),
    ],
)
def test_dotProduct(nums1: List[int], nums2: List[int], expected: int):
    assert SparseVector(nums1).dotProduct(SparseVector(nums2)) == expected
