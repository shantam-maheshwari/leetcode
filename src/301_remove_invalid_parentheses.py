from typing import List

import pytest

# # dfs (backtracking)
# from typing import Tuple, Set
# class Solution:
#     def removeInvalidParentheses(self, s: str) -> List[str]:
#         def minParensToRemove(s: str) -> Tuple[int, int]:
#             left = right = 0
#             for c in s:
#                 if c == "(":
#                     left += 1
#                 elif c == ")":
#                     if left > 0:
#                         left -= 1
#                     else:
#                         right += 1

#             return (left, right)

#         def backtrack(
#             i: int,
#             left: int,
#             right: int,
#             balance: int,
#             candidate: str,
#             result: Set[str],
#         ):
#             if i == len(s):
#                 if left == 0 and right == 0 and balance == 0:
#                     result.add(candidate)
#                 return

#             if s[i] == "(":
#                 # include s[i]
#                 backtrack(i + 1, left, right, balance + 1, candidate + "(", result)

#                 # exclude s[i]
#                 if left > 0:
#                     backtrack(i + 1, left - 1, right, balance, candidate, result)

#             elif s[i] == ")":
#                 # include s[i]
#                 if balance > 0:
#                     backtrack(i + 1, left, right, balance - 1, candidate + ")", result)

#                 # exclude s[i]
#                 if right > 0:
#                     backtrack(i + 1, left, right - 1, balance, candidate, result)

#             else:
#                 backtrack(i + 1, left, right, balance, candidate + s[i], result)

#         left, right = minParensToRemove(s)
#         result = set()
#         backtrack(0, left, right, 0, "", result)
#         return list(result)


# bfs
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s: str) -> bool:
            balance = 0
            for c in s:
                if c == "(":
                    balance += 1
                elif c == ")":
                    if balance > 0:
                        balance -= 1
                    else:
                        return False
            return balance == 0

        curr_level = set([s])

        while True:
            valid_strings = list(filter(isValid, curr_level))
            if len(valid_strings) > 0:
                return valid_strings

            next_level = set()
            for string in curr_level:
                for i in range(len(string)):
                    next_level.add(string[:i] + string[i + 1 :])

            curr_level = next_level


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("()())()", ["(())()", "()()()"]),
        ("()())()", ["(())()", "()()()"]),
        (")(", [""]),
    ],
)
def test_removeInvalidParentheses(s: str, expected: List[str]):
    assert set(Solution().removeInvalidParentheses(s)) == set(expected)
