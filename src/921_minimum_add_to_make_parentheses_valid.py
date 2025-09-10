import pytest


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        missing_closing_brackets = 0

        for c in s:
            if c == "(":
                open_brackets += 1
            elif open_brackets == 0:
                missing_closing_brackets += 1
            else:
                open_brackets -= 1

        return open_brackets + missing_closing_brackets


@pytest.mark.parametrize(("s", "expected"), [("())", 1), ("(((", 3)])
def test_minAddToMakeValid(s: str, expected: int):
    assert Solution().minAddToMakeValid(s) == expected
