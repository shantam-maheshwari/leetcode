from typing import List

import pytest


class Solution:
    # # time complexity: O(n)
    # def findKthPositive(self, arr: List[int], k: int) -> int:
    #     missing_count = 0

    #     prev = 0
    #     for num in arr:
    #         diff = num - prev - 1
    #         if missing_count + diff >= k:
    #             return prev + (k - missing_count)

    #         missing_count += diff
    #         prev = num

    #     return prev + (k - missing_count)

    # time complexity: O(log(n))
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k

        left = 0
        right = len(arr) - 1

        def missing_count(i: int) -> int:
            return arr[i] - i - 1

        while left < right:
            mid = (left + right + 1) // 2
            if missing_count(mid) >= k:
                right = mid - 1
            else:
                left = mid
        return arr[left] + k - missing_count(left)


@pytest.mark.parametrize(
    ("arr", "k", "expected"),
    [([2, 3, 4, 7, 11], 5, 9), ([1, 2, 3, 4], 2, 6), ([1, 3], 1, 2)],
)
def test_findKthPositive(arr: List[int], k: int, expected: int):
    assert Solution().findKthPositive(arr, k) == expected
