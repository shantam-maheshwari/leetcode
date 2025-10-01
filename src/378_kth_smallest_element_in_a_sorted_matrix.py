from heapq import heappop, heappush
from typing import List

import pytest


# Tip: First solve 240. Search a 2D Matrix II to build intuition for min heap solution.
class Solution:
    # max heap
    # time complexity: O(M * N * log(k))
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush(heap, -matrix[i][j])
                if len(heap) == k + 1:
                    heappop(heap)

        return -heappop(heap)

    # min heap
    # time complexity: O(min(m, k) + k*log(min(m, k)))
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        heap = []
        for i in range(min(m, k)):
            heappush(heap, (matrix[i][0], i, 0))

        for _ in range(k - 1):
            _ele, r, c = heappop(heap)

            if c < n - 1:
                heappush(heap, (matrix[r][c + 1], r, c + 1))

        return heappop(heap)[0]

    # binary search on the range of values i.e. [matrix[0][0], matrix[-1][-1]]
    # time complexity: O(log(max_val - min_val) * m * log(n))
    # Q: how is `left` guaranteed to be an element in the matrix?
    # A: `left` is the **smallest number** such that countLessOrEqual() == k

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:
            mid = (left + right) // 2
            count = self._countLessOrEqual(mid, matrix)
            if count < k:
                left = mid + 1
            else:
                right = mid

        return left

    def _countLessOrEqual(self, num: int, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        count = 0
        for r in range(m):
            if matrix[r][0] > num:
                break

            left = 0
            right = n - 1
            while left < right:
                mid = (left + right + 1) // 2
                if matrix[r][mid] > num:
                    right = mid - 1
                else:
                    left = mid
            count += left + 1

        return count


@pytest.mark.parametrize(
    ("matrix", "k", "expected"),
    [([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13), ([[-5]], 1, -5)],
)
def test_kthSmallest(matrix: List[List[int]], k: int, expected: int):
    assert Solution().kthSmallest(matrix, k) == expected
