from typing import List

import pytest


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(i: int, j: int, color: int) -> int:
            """color island with given color"""
            grid[i][j] = color
            curr_size = 1

            steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for step in steps:
                i1 = i + step[0]
                j1 = j + step[1]

                if 0 <= i1 < len(grid) and 0 <= j1 < len(grid[i]) and grid[i1][j1] == 1:
                    curr_size += dfs(i1, j1, color)

            return curr_size

        color = 2
        island_sizes = {}  # color -> size

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    island_sizes[color] = dfs(i, j, color)
                    color += 1

        print(island_sizes)

        # if 0 islands
        if color == 2:
            return 1

        # if whole grid can be a single island
        if color == 3:
            return min(island_sizes[2] + 1, len(grid) * len(grid[0]))

        island_sizes[0] = 0
        max_size = 0
        steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    curr_size = 0

                    seen = set()
                    for step in steps:
                        i1 = i + step[0]
                        j1 = j + step[1]

                        if 0 <= i1 < len(grid) and 0 <= j1 < len(grid[i]):
                            curr_color = grid[i1][j1]
                            if curr_color not in seen:
                                curr_size += island_sizes[curr_color]
                                seen.add(curr_color)

                    max_size = max(max_size, curr_size + 1)

        return max_size


@pytest.mark.parametrize(
    ("grid", "expected"),
    [([[1, 0], [0, 1]], 3), ([[1, 1], [1, 0]], 4), ([[1, 1], [1, 1]], 4)],
)
def test_largestIsland(grid: List[List[int]], expected: int):
    assert Solution().largestIsland(grid) == expected
