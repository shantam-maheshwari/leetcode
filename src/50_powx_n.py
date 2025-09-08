import pytest


class Solution:
    # # space: O(log(n))
    # def myPow(self, x: float, n: int) -> float:
    #     if n == 0:
    #         return 1
    #     if n < 0:
    #         return self.myPow(1 / x, -n)

    #     result = self.myPow(x, n // 2)
    #     result *= result

    #     return result if n % 2 == 0 else result * x

    # space optimized, space: O(1)
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            n = -n
            x = 1 / x

        result = 1
        while n:
            if n % 2 == 1:
                result *= x
                n -= 1

            n //= 2
            x *= x
        return result


@pytest.mark.parametrize(
    ("x", "n", "expected"), [(2, 9, 512), (2.1, 3, 9.261), (2, -2, 0.25)]
)
def test_myPow(x: float, n: float, expected: float):
    assert Solution().myPow(x, n) == pytest.approx(expected)
