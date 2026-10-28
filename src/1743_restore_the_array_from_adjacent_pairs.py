from collections import defaultdict
from typing import List

import pytest


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # create graph
        # find nums that only have 1 neighbour
        # traverse from one such num

        graph = defaultdict(list)
        for [a, b] in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)

        start_num = 0
        for num, neighbours in graph.items():
            if len(neighbours) == 1:
                start_num = num
                break

        result = [start_num]

        def dfs(prev: int, curr: int):
            for num in graph[curr]:
                if num != prev:
                    result.append(num)
                    dfs(curr, num)

        dfs(None, start_num)

        return result


@pytest.mark.parametrize(
    ("adjacentPairs", "expected"),
    [
        ([[2, 1], [3, 4], [3, 2]], [1, 2, 3, 4]),
        ([[4, -2], [1, 4], [-3, 1]], [-2, 4, 1, -3]),
        ([[100000, -100000]], [100000, -100000]),
    ],
)
def test_restoreArray(adjacentPairs: List[List[int]], expected: List):
    result = Solution().restoreArray(adjacentPairs)
    assert result in [expected, reversed(expected)]
