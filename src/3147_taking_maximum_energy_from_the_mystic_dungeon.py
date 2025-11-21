from typing import List

import pytest


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        result = float("-inf")

        i = len(energy) - 1
        while i >= len(energy) - k:
            curr_sum = 0
            j = i
            while j >= 0:
                curr_sum += energy[j]
                result = max(result, curr_sum)
                j -= k
            i -= 1

        return result


@pytest.mark.parametrize(
    ("energy", "k", "expected"), [([5, 2, -10, -5, 1], 3, 3), ([-2, -3, -1], 2, -1)]
)
def test_maximumEnergy(energy: List[int], k: int, expected: int):
    assert Solution().maximumEnergy(energy, k) == expected
