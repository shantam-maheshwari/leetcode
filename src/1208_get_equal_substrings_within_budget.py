import pytest


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [0] * len(s)
        for i in range(len(s)):
            costs[i] = abs(ord(s[i]) - ord(t[i]))

        # max subarray with sum at most k
        max_length = 0
        left = right = 0
        curr_sum = 0
        while right < len(costs):
            curr_sum += costs[right]

            while curr_sum > maxCost and left <= right:
                curr_sum -= costs[left]
                left += 1

            length = right - left + 1
            max_length = max(max_length, length)

            right += 1

        return max_length


@pytest.mark.parametrize(
    ("s", "t", "maxCost", "expected"),
    [("abcd", "bcdf", 3, 3), ("abcd", "cdef", 3, 1), ("abcd", "acde", 0, 1)],
)
def test_equalSubstring(s: str, t: str, maxCost: int, expected: int):
    assert Solution().equalSubstring(s, t, maxCost) == expected
