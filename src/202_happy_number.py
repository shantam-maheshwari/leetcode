import pytest

# 2
# 4
# 16
# 37
# 58
# 64 + 25 = 89
# 64 + 81 = 145
# 1 + 16 + 25 = 42
# 16 + 4 = 20
# 4


class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares_of_digits(n: int) -> int:
            result = 0
            while n:
                digit = n % 10
                result += digit * digit
                n //= 10
            return result

        while n != 1 and n != 4:
            n = sum_of_squares_of_digits(n)
        return n == 1


@pytest.mark.parametrize(("n", "expected"), [(19, True), (2, False)])
def test_isHappy(n: int, expected: bool):
    assert Solution().isHappy(n) == expected
