import pytest


class Solution:
    def findComplement(self, num: int) -> int:
        # decimal to binary
        bin = []
        while num:
            digit = num % 2
            bin.append(digit)
            num //= 2

        # complement
        for i in range(len(bin)):
            bin[i] = 1 - bin[i]

        # binary to decimal
        factor = 1
        dec = 0
        for i in range(len(bin)):
            dec += bin[i] * factor
            factor *= 2

        return dec


@pytest.mark.parametrize(("num", "expected"), [(5, 2), (1, 0)])
def test_findComplement(num: int, expected: int):
    assert Solution().findComplement(num) == expected
