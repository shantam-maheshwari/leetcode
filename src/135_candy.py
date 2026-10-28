from typing import List

import pytest


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        # first pass: left to right
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # second pass: right to left
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)


@pytest.mark.parametrize(("ratings", "expected"), [([1, 0, 2], 5), ([1, 2, 2], 4)])
def test_candy(ratings: List[int], expected: int):
    assert Solution().candy(ratings) == expected
