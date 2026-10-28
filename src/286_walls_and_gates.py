from collections import deque
from typing import List

import pytest


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        queue = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                # i, j is a gate
                if rooms[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        distance = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = min(rooms[r][c], distance)

                for x, y in steps:
                    r1 = r + x
                    c1 = c + y

                    if (
                        0 <= r1 < m
                        and 0 <= c1 < n
                        and (r1, c1) not in visited
                        and rooms[r1][c1] > 0
                    ):
                        visited.add((r1, c1))
                        queue.append((r1, c1))

            distance += 1


@pytest.mark.parametrize(
    ("rooms", "expected"),
    [
        (
            [
                [2147483647, -1, 0, 2147483647],
                [2147483647, 2147483647, 2147483647, -1],
                [2147483647, -1, 2147483647, -1],
                [0, -1, 2147483647, 2147483647],
            ],
            [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]],
        ),
        ([[-1]], [[-1]]),
    ],
)
def test_wallsAndGates(rooms: List[List[int]], expected: List[List[int]]):
    Solution().wallsAndGates(rooms)
    assert rooms == expected
