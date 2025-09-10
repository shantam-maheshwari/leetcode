import pytest


class Solution:
    def isValid(self, s: str) -> bool:
        closing_parens = {"(": ")", "[": "]", "{": "}"}

        stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
                continue
            elif not stack or closing_parens[stack.pop()] != c:
                return False

        return len(stack) == 0


@pytest.mark.parametrize(
    ("s", "expected"), [("()", True), ("()[]{}", True), ("(]", False)]
)
def test_isValid(s: str, expected: bool):
    assert Solution().isValid(s) == expected
