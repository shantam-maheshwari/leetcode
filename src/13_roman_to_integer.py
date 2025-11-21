import pytest


class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        for c in reversed(s):
            if c == "I":
                if integer < 5:
                    integer += 1
                else:
                    integer -= 1
            elif c == "V":
                integer += 5
            elif c == "X":
                if integer < 50:
                    integer += 10
                else:
                    integer -= 10
            elif c == "L":
                integer += 50
            elif c == "C":
                if integer < 500:
                    integer += 100
                else:
                    integer -= 100
            elif c == "D":
                integer += 500
            else:
                integer += 1000

        return integer


@pytest.mark.parametrize(
    ("s", "expected"), [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)]
)
def test_romanToInt(s: str, expected: int):
    assert Solution().romanToInt(s) == expected
