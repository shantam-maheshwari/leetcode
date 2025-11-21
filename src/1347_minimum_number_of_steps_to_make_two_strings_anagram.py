import pytest

# from typing import List
# class Solution:
#     def minSteps(self, s: str, t: str) -> int:
#         s_char_counts = self.char_counts(s)
#         t_char_counts = self.char_counts(t)

#         diffs = [abs(x - y) for x, y in zip(s_char_counts, t_char_counts)]
#         return sum(diffs) // 2

#     def char_counts(self, s: str) -> List[int]:
#         counts = [0] * 26
#         for c in s:
#             counts[ord(c) - ord("a")] += 1
#         return counts


# space optimized
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_counts = [0] * 26
        for c in s:
            char_counts[ord(c) - ord("a")] += 1
        for c in t:
            char_counts[ord(c) - ord("a")] -= 1

        result = 0
        for x in char_counts:
            if x > 0:
                result += x
        return result


@pytest.mark.parametrize(
    ("s", "t", "expected"),
    [("bab", "aba", 1), ("leetcode", "practice", 5), ("anagram", "mangaar", 0)],
)
def test_minSteps(s: str, t: str, expected: int):
    assert Solution().minSteps(s, t) == expected
