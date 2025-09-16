from typing import List

import pytest


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        m = len(matrix)
        n = len(matrix[0])

        first_row_contains_zero = False
        first_col_contains_zero = False

        for j in range(n):
            if matrix[0][j] == 0:
                first_row_contains_zero = True
                break

        for i in range(m):
            if matrix[i][0] == 0:
                first_col_contains_zero = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_contains_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_contains_zero:
            for i in range(m):
                matrix[i][0] = 0


@pytest.mark.parametrize(
    ("matrix", "expected"),
    [
        (
            [
                # noqa
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1],
            ],
            [
                # noqa
                [1, 0, 1],
                [0, 0, 0],
                [1, 0, 1],
            ],
        ),
        (
            [
                # noqa
                [0, 1, 2, 0],
                [3, 4, 5, 2],
                [1, 3, 1, 5],
            ],
            [
                # noqa
                [0, 0, 0, 0],
                [0, 4, 5, 0],
                [0, 3, 1, 0],
            ],
        ),
    ],
)
def test_setZeroes(matrix: List[List[int]], expected: List[List[int]]):
    Solution().setZeroes(matrix)
    assert matrix == expected
