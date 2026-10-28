from typing import List

import pytest

# class Solution:
#     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         m = len(matrix)
#         n = len(matrix[0])

#         # bottom left triangle
#         for i in range(m):
#             row = i
#             col = 0
#             num = matrix[row][col]
#             while row < m and col < n:
#                 if matrix[row][col] != num:
#                     return False
#                 row += 1
#                 col += 1

#         # upper right triangle
#         for i in range(1, n):
#             row = 0
#             col = i
#             num = matrix[row][col]
#             while row < m and col < n:
#                 if matrix[row][col] != num:
#                     return False
#                 row += 1
#                 col += 1

#         return True


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False

        return True


@pytest.mark.parametrize(
    ("matrix", "expected"),
    [([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True), ([[1, 2], [2, 2]], False)],
)
def test_isToeplitzMatrix(matrix: List[List[int]], expected: bool):
    assert Solution().isToeplitzMatrix(matrix) == expected
