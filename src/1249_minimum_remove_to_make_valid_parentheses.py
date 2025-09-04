from typing import List

import pytest


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        stack = []

        for i, c in enumerate(s_list):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    s_list[i] = ""

        while stack:
            s_list[stack.pop()] = ""

        return "".join(s_list)


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
