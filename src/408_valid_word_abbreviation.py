import pytest


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isdigit():
                num_idx = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                i += int(abbr[num_idx:j])
            else:
                return False

        return i == len(word) and j == len(abbr)


@pytest.mark.parametrize(
    ("word", "abbr", "expected"),
    [
        ("substitution", "s10n", True),
        ("substitution", "sub4u4", True),
        ("substitution", "12", True),
        ("internationalization", "i12iz4n", True),
        ("apple", "a2e", False),
        ("abbde", "a1b01e", False),
        ("hi", "1hi", False),
    ],
)
def test_validWordAbbreviation(word: str, abbr: str, expected: bool):
    assert Solution().validWordAbbreviation(word, abbr) == expected
