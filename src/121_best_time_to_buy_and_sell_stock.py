from typing import List

import pytest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit


@pytest.mark.parametrize(
    ("prices", "expected"), [([7, 1, 5, 3, 6, 4], 5), ([7, 6, 4, 3, 1], 0)]
)
def test_maxProfit(prices: List[int], expected: int):
    assert Solution().maxProfit(prices) == expected
