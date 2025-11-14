from typing import List

import pytest

# # stack
# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         s_list = list(s)
#         stack = []

#         for i, c in enumerate(s_list):
#             if c == "(":
#                 stack.append(i)
#             elif c == ")":
#                 if stack:
#                     stack.pop()
#                 else:
#                     s_list[i] = ""

#         while stack:
#             s_list[stack.pop()] = ""

#         return "".join(s_list)


# two pass
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = self.removeUnmatchedOpenBrackets(s, "(", ")")
        s = self.removeUnmatchedOpenBrackets(s[::-1], ")", "(")
        return s[::-1]

    def removeUnmatchedOpenBrackets(
        self, s: str, open_bracket: str, close_bracket: str
    ) -> str:
        result = ""

        balance = 0
        for c in s:
            if c == open_bracket:
                balance += 1
            elif c == close_bracket:
                if balance > 0:
                    balance -= 1
                else:
                    continue
            result += c

        return result


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("lee(t(c)o)de)", ["lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"]),
        ("a)b(c)d", ["ab(c)d"]),
        ("))((", [""]),
    ],
)
def test_minRemoveToMakeValid(s: str, expected: List[str]):
    assert Solution().minRemoveToMakeValid(s) in set(expected)
