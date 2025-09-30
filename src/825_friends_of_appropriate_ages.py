from typing import List

import pytest


class Solution:
    # # N: len(ages)
    # # time complexity: N * log(N)
    # def numFriendRequests(self, ages: List[int]) -> int:
    #     ages = sorted(ages)

    #     requests = 0
    #     for x, x_age in enumerate(ages):
    #         lb = binary_search_left(ages, x_age // 2 + 8)
    #         ub = binary_search_right(ages, x_age)
    #         if lb != -1 and ub != -1:
    #             requests += max(0, ub - lb)

    #     return requests

    # N: len(ages)
    # A: 121 (age range)
    # time complexity: N + A**2
    def numFriendRequests(self, ages: List[int]) -> int:
        counts = [0] * 121
        for age in ages:
            counts[age] += 1

        requests = 0
        for x, x_count in enumerate(counts):
            for y, y_count in enumerate(counts):
                if (y > x // 2 + 7) and (y <= x):
                    if x == y:
                        requests += x_count * (x_count - 1)
                    else:
                        requests += x_count * y_count

        return requests


def binary_search_left(nums: List[int], target: int) -> int:
    if not nums or nums[-1] < target:
        return -1

    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def binary_search_right(nums: List[int], target: int) -> int:
    if not nums or nums[0] > target:
        return -1

    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid
    return left


@pytest.mark.parametrize(
    ("ages", "expected"),
    [([16, 16], 2), ([16, 17, 18], 2), ([20, 30, 100, 110, 120], 3)],
)
def test_numFriendRequests(ages: List[int], expected: int):
    assert Solution().numFriendRequests(ages) == expected
