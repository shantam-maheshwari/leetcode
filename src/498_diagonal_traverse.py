from typing import List

import pytest


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []

        m = len(mat)
        n = len(mat[0])
        result = []

        r = 0
        c = 0
        direction = 1  # -1 means down, 1 means up

        while len(result) < m * n:
            result.append(mat[r][c])

            if direction == 1:
                if c == n - 1:
                    r += 1
                    direction = -1
                elif r == 0:
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                    direction = 1
                elif c == 0:
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1

        return result


@pytest.mark.parametrize(
    ("mat", "expected"),
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
    ],
)
def test_findDiagonalOrder(mat: List[List[int]], expected: List[int]):
    assert Solution().findDiagonalOrder(mat) == expected
