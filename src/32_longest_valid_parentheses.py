import pytest

# # sliding window
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         max_length = 0

#         # sliding window from left to right
#         left = right = 0
#         for c in s:
#             if c == "(":
#                 left += 1
#             else:
#                 right += 1

#             if left == right:
#                 length = left + right
#                 max_length = max(max_length, length)
#             elif left < right:
#                 left = right = 0

#         # sliding window from right to left
#         left = right = 0
#         for c in reversed(s):
#             if c == ")":
#                 right += 1
#             else:
#                 left += 1

#             if left == right:
#                 length = left + right
#                 max_length = max(max_length, length)
#             elif left > right:
#                 left = right = 0

#         return max_length


# stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        valid = [False] * len(s)
        stack = []

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif len(stack) > 0:
                valid[i] = True
                valid[stack.pop()] = True

        max_length = 0
        length = 0
        for i, v in enumerate(valid):
            if v:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 0

        return max_length


@pytest.mark.parametrize(("s", "expected"), [("(()", 2), (")()())", 4), ("", 0)])
def test_longestValidParentheses(s: str, expected: int):
    assert Solution().longestValidParentheses(s) == expected
