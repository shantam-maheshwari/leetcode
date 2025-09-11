from collections import deque

import pytest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = deque()

        i1 = len(num1) - 1
        i2 = len(num2) - 1

        sum = 0
        carry = 0
        while i1 >= 0 or i2 >= 0 or carry:
            n1 = 0
            if i1 >= 0:
                n1 = ord(num1[i1]) - ord("0")
                i1 -= 1

            n2 = 0
            if i2 >= 0:
                n2 = ord(num2[i2]) - ord("0")
                i2 -= 1

            sum = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) // 10
            result.appendleft(str(sum))

        return "".join(list(result))

    # Meta follow up question: make it work for decimals
    # e.g. "1234" and "3.1457"

    def addStringsDecimal(self, num1: str, num2: str) -> str:
        decimal1 = 0
        i1 = len(num1) - 1
        while i1 >= 0 and num1[i1] != ".":
            i1 -= 1
        if i1 != -1:
            num1 = num1[:i1] + num1[i1 + 1 :]
            decimal1 = len(num1) - i1

        decimal2 = 0
        i2 = len(num1) - 1
        while i2 >= 0 and num2[i2] != ".":
            i2 -= 1
        if i2 != -1:
            num2 = num2[:i2] + num2[i2 + 1 :]
            decimal2 = len(num2) - i2

        # ensure num1 has more decimal places than num2
        if decimal2 > decimal1:
            decimal1, decimal2 = decimal2, decimal1
            num1, num2 = num2, num1

        if decimal1:
            num2 = num2 + "".join(["0"] * (decimal1 - decimal2))

        result = self.addStrings(num1, num2)

        if decimal1:
            result = result[:-decimal1] + "." + result[-decimal1:]

        return result


@pytest.mark.parametrize(
    ("num1", "num2", "expected"),
    [("11", "123", "134"), ("456", "77", "533"), ("0", "0", "0")],
)
def test_addStrings(num1: str, num2: str, expected: str):
    assert Solution().addStrings(num1, num2) == expected


@pytest.mark.parametrize(
    ("num1", "num2", "expected"),
    [("1234", "3.1457", "1237.1457")],
)
def test_addStringsDecimal(num1: str, num2: str, expected: str):
    assert Solution().addStringsDecimal(num1, num2) == expected


# See also:

# Strings
# 67. Add Binary: sum two binary strings.
# 415. Add Strings (current): sum two non-negative numbers in a string representation without converting them to integers directly.

# Integers
# 371. Sum of Two Integers: Sum two integers without using + and - operators.

# Arrays
# 989. Add to Array-Form of Integer: Textbook addition

# Linked Lists: Sentinel Head + Textbook Addition
# 66. Plus One
# 2. Add Two Numbers
# 445. Add Two Numbers II
