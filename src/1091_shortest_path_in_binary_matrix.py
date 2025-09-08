from collections import deque
from typing import List

import pytest


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if n == 0 or grid[0][0] == 1:
            return -1

        queue = deque()
        queue.append((0, 0))
        grid[0][0] = 1
        next_steps = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
        ]
        distance = 1

        while queue:
            for _ in range(len(queue)):
                curr_x, curr_y = queue.popleft()
                if curr_x == n - 1 and curr_y == n - 1:
                    return distance

                for step in next_steps:
                    next_x = curr_x + step[0]
                    next_y = curr_y + step[1]

                    if (
                        next_x >= 0
                        and next_x < n
                        and next_y >= 0
                        and next_y < n
                        and grid[next_x][next_y] == 0
                    ):
                        grid[next_x][next_y] = 1
                        queue.append((next_x, next_y))
            distance += 1

        return -1


@pytest.mark.parametrize(
    ("grid", "expected"),
    [
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
    ],
)
def test_shortestPathBinaryMatrix(grid: List[List[int]], expected: int):
    assert Solution().shortestPathBinaryMatrix(grid) == expected
