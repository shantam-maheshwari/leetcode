import pytest


class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     max_length = 0

    #     left = 0
    #     right = 0
    #     seen = set()
    #     while right < len(s):
    #         while s[right] in seen:
    #             seen.remove(s[left])
    #             left += 1

    #         seen.add(s[right])
    #         max_length = max(max_length, right - left + 1)
    #         right += 1

    #     return max_length

    # optimized
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        left = 0
        right = 0
        last_seen = {}
        while right < len(s):
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]] + 1

            max_length = max(max_length, right - left + 1)
            last_seen[s[right]] = right
            right += 1

        return max_length


@pytest.mark.parametrize(
    ("s", "expected"), [("abcabcbb", 3), ("bbbbb", 1), ("pwwkew", 3)]
)
def test_lengthOfLongestSubstring(s: str, expected: int):
    assert Solution().lengthOfLongestSubstring(s) == expected
