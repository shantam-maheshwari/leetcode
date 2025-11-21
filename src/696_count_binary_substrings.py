import pytest

# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         result = 0

#         i = 0
#         while i < len(s):
#             zeros = 0
#             ones = 0

#             if s[i] == "0":
#                 j = i
#                 while j < len(s) and s[j] == "0":
#                     zeros += 1
#                     j += 1
#                 while j < len(s) and s[j] == "1":
#                     ones += 1
#                     j += 1
#                 result += min(zeros, ones)
#                 i += zeros
#             else:
#                 j = i
#                 while j < len(s) and s[j] == "1":
#                     ones += 1
#                     j += 1
#                 while j < len(s) and s[j] == "0":
#                     zeros += 1
#                     j += 1
#                 result += min(zeros, ones)
#                 i += ones

#         return result


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        for i in range(len(s)):
            if i == 0:
                groups.append(1)
            elif s[i] == s[i - 1]:
                groups[-1] += 1
            else:
                groups.append(1)

        result = 0
        for i in range(1, len(groups)):
            result += min(groups[i - 1], groups[i])

        return result


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("00110011", 6),
        ("10101", 4),
    ],
)
def test_countBinarySubstrings(s: str, expected: int):
    assert Solution().countBinarySubstrings(s) == expected
