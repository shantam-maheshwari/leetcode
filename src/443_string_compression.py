from typing import List

import pytest


class Solution:
    def compress(self, chars: List[str]) -> int:
        chars += "*"

        i = 1
        j = 0
        last_char_seen = chars[0]
        count = 1
        while i < len(chars):
            if chars[i] == last_char_seen:
                count += 1
                i += 1
                continue

            chars[j] = last_char_seen
            j += 1
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[j] = digit
                    j += 1

            last_char_seen = chars[i]
            count = 1
            i += 1

        return j


@pytest.mark.parametrize(
    ("chars", "expected_chars", "expected_len"),
    [
        (["a", "a", "b", "b", "c", "c", "c"], ["a", "2", "b", "2", "c", "3"], 6),
        (["a"], ["a"], 1),
        (
            ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
            ["a", "b", "1", "2"],
            4,
        ),
    ],
)
def test_compress(chars: List[str], expected_chars: List[str], expected_len: int):
    assert Solution().compress(chars) == expected_len
    assert chars[:expected_len] == expected_chars
