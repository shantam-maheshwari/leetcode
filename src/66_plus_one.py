from typing import List

import pytest


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0
            i -= 1

        digits.insert(0, 1)
        return digits


@pytest.mark.parametrize(
    ("digits", "expected"),
    [([1, 2, 3], [1, 2, 4]), ([4, 3, 2, 1], [4, 3, 2, 2]), ([9], [1, 0])],
)
def test_plusOne(digits: List[int], expected: List[int]):
    assert Solution().plusOne(digits) == expected
