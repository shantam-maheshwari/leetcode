from typing import List

import pytest


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        prev = [1]

        for i in range(numRows):
            curr = [1] * (i + 1)
            for j in range(1, i):
                curr[j] = prev[j - 1] + prev[j]
            result.append(curr)
            prev = curr

        return result


@pytest.mark.parametrize(
    ("numRows", "expected"),
    [(5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]), (1, [[1]])],
)
def test_generate(numRows: int, expected: List[List[int]]):
    assert Solution().generate(numRows) == expected
