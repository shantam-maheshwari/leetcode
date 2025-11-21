from typing import List

import pytest

# # min heap, time: O(n.log(n))
# import heapq
# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#         intervals = sorted(intervals)
#         heap = []
#         result = 0

#         for [start, end] in intervals:
#             if not heap:
#                 heapq.heappush(heap, end)
#             else:
#                 while heap and heap[0] <= start:
#                     heapq.heappop(heap)
#                 heapq.heappush(heap, end)

#             result = max(result, len(heap))
#         return result


# time: O(n.log(n))
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([start for [start, _] in intervals])
        ends = sorted([end for [_, end] in intervals])

        i = j = 0
        max_overlap = 0
        curr_overlap = 0

        while i < len(starts) and j < len(ends):
            if starts[i] < ends[j]:
                curr_overlap += 1
                max_overlap = max(max_overlap, curr_overlap)
                i += 1
            else:
                curr_overlap -= 1
                j += 1

        return max_overlap


@pytest.mark.parametrize(
    ("intervals", "expected"),
    [([[0, 30], [5, 10], [15, 20]], 2), ([[7, 10], [2, 4]], 1)],
)
def test_minMeetingRooms(intervals: List[List[int]], expected: int):
    assert Solution().minMeetingRooms(intervals) == expected
