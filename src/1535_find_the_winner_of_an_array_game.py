from typing import List

import pytest

# # time: O(n), space: O(n)
# class Solution:
#     def getWinner(self, arr: List[int], k: int) -> int:
#         max_element = max(arr)
#         queue = arr

#         wins = 0
#         while wins < k and queue[0] != max_element:
#             if queue[0] > queue[1]:
#                 num = queue.pop(1)
#                 wins += 1
#             else:
#                 num = queue.pop(0)
#                 wins = 1
#             queue.append(num)

#         return queue[0]


# time: O(n), space: O(1)
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        wins = 0
        candidate = 0
        for i in range(1, len(arr)):
            if arr[candidate] > arr[i]:
                wins += 1
            else:
                candidate = i
                wins = 1

            if wins == k:
                return arr[candidate]

        return arr[candidate]


@pytest.mark.parametrize(
    ("arr", "k", "expected"), [([2, 1, 3, 5, 4, 6, 7], 2, 5), ([3, 2, 1], 10, 3)]
)
def test_getWinner(arr: List[int], k: int, expected: int):
    assert Solution().getWinner(arr, k) == expected
