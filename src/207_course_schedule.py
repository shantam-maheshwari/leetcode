from collections import defaultdict, deque
from typing import List

import pytest


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degrees = [0] * numCourses
        for [a, b] in prerequisites:
            graph[b].append(a)
            in_degrees[a] += 1

        queue = deque()
        for u, degree in enumerate(in_degrees):
            if degree == 0:
                queue.append(u)

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    queue.append(v)

        return sum(in_degrees) == 0


@pytest.mark.parametrize(
    ("numCourses", "prerequisites", "expected"),
    [(2, [[1, 0]], True), (2, [[1, 0], [0, 1]], False)],
)
def test_canFinish(numCourses: int, prerequisites: List[List[int]], expected: bool):
    assert Solution().canFinish(numCourses, prerequisites) == expected
