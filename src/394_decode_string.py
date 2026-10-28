import pytest


class Solution:
    def decodeString(self, s: str) -> str:
        count = []
        token = []

        curr_token = ""
        curr_count = 0

        for c in s:
            if c.isdigit():
                curr_count = curr_count * 10 + int(c)
                continue

            if c.isalpha():
                curr_token += c
                continue

            if c == "[":
                count.append(curr_count)
                curr_count = 0

                token.append(curr_token)
                curr_token = ""
                continue

            if c == "]":
                prev_token = token.pop()
                curr_token = prev_token + (curr_token * count.pop())

        return curr_token


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
    ],
)
def test_decodeString(s: str, expected: str):
    assert Solution().decodeString(s) == expected
