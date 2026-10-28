import pytest

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.strip()
#         words = s.split(" ")
#         return len(words[-1])


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1

        j = i
        while i >= 0 and s[i] != " ":
            i -= 1

        return j - i


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
    ],
)
def test_lengthOfLastWord(s: str, expected: int):
    assert Solution().lengthOfLastWord(s) == expected
