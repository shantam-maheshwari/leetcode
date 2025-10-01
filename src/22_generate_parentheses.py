from collections import deque
from typing import List

import pytest


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        queue = deque()
        queue.append(("(", 1, 1))

        while queue:
            candidate, opened, balance = queue.popleft()

            if len(candidate) == 2 * n:
                result.append(candidate)

            if opened < n:
                queue.append((candidate + "(", opened + 1, balance + 1))
            if balance > 0:
                queue.append((candidate + ")", opened, balance - 1))

        return result


@pytest.mark.parametrize(
    ("n", "expected"),
    [(3, ["((()))", "(()())", "(())()", "()(())", "()()()"]), (1, ["()"])],
)
def test_generateParenthesis(n: int, expected: int):
    assert set(Solution().generateParenthesis(n)) == set(expected)
