from typing import List

import pytest


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        result = [intervals[0]]
        for [start, end] in intervals[1:]:
            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        return result


@pytest.mark.parametrize(
    ("intervals", "expected"),
    [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[4, 7], [1, 4]], [[1, 7]]),
    ],
)
def test_merge(intervals: List[List[int]], expected: List[List[int]]):
    assert Solution().merge(intervals) == expected
