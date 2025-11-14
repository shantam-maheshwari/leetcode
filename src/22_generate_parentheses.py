from collections import deque
from typing import List

import pytest

# # bfs
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         result = []

#         queue = deque()
#         queue.append(("(", 1, 1))

#         while queue:
#             candidate, opened, balance = queue.popleft()

#             if len(candidate) == 2 * n:
#                 result.append(candidate)

#             if opened < n:
#                 queue.append((candidate + "(", opened + 1, balance + 1))
#             if balance > 0:
#                 queue.append((candidate + ")", opened, balance - 1))

#         return result


# backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(candidate: str, left: int, right: int):
            if left == 0 and right == 0:
                result.append(candidate)
                return

            # add left bracket
            if left > 0:
                backtrack(candidate + "(", left - 1, right)

            # add right bracket
            if left < right:
                backtrack(candidate + ")", left, right - 1)

        backtrack("", n, n)
        return result


@pytest.mark.parametrize(
    ("n", "expected"),
    [(3, ["((()))", "(()())", "(())()", "()(())", "()()()"]), (1, ["()"])],
)
def test_generateParenthesis(n: int, expected: int):
    assert set(Solution().generateParenthesis(n)) == set(expected)
