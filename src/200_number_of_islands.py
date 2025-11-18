from collections import deque
from typing import List

import pytest

# # dfs
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         result = 0

#         def dfs(i: int, j: int):
#             if (
#                 i >= 0
#                 and i < len(grid)
#                 and j >= 0
#                 and j < len(grid[0])
#                 and grid[i][j] == "1"
#             ):
#                 grid[i][j] = "0"
#                 dfs(i - 1, j)
#                 dfs(i + 1, j)
#                 dfs(i, j - 1)
#                 dfs(i, j + 1)

#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == "1":
#                     dfs(i, j)
#                     result += 1

#         return result


# bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result += 1

                    queue = deque()
                    queue.append((i, j))
                    while queue:
                        u, v = queue.popleft()
                        if (
                            u >= 0
                            and u < len(grid)
                            and v >= 0
                            and v < len(grid[0])
                            and grid[u][v] == "1"
                        ):
                            grid[u][v] = "0"
                            for x, y in steps:
                                queue.append((u + x, v + y))

        return result


@pytest.mark.parametrize(
    ("grid", "expected"),
    [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
    ],
)
def test_numIslands(grid: List[List[str]], expected):
    assert Solution().numIslands(grid) == expected
