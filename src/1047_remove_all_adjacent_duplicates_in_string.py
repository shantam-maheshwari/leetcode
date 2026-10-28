import pytest


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s:
            if not stack:
                stack.append(c)
                continue

            if c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


@pytest.mark.parametrize(("s", "expected"), [("abbaca", "ca"), ("azxxzy", "ay")])
def test_removeDuplicates(s: str, expected: str):
    assert Solution().removeDuplicates(s) == expected
