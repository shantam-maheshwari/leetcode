from bisect import bisect_left
from typing import List

import pytest


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        results = []
        products = sorted(products)

        for i in range(len(searchWord)):
            start_idx = bisect_left(products, searchWord[: i + 1])  # optimization

            result = [
                product
                for product in products[start_idx:]
                if product[: i + 1] == searchWord[: i + 1]
            ]
            results.append(result[: min(3, len(result))])
            products = result  # optimization

        return results


@pytest.mark.parametrize(
    ("products", "searchWord", "expected"),
    [
        (
            ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
            "mouse",
            [
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
        ),
        (
            ["havana"],
            "havana",
            [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]],
        ),
    ],
)
def test_suggestedProducts(
    products: List[str], searchWord: str, expected: List[List[str]]
):
    assert Solution().suggestedProducts(products, searchWord) == expected
