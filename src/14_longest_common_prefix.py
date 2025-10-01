from typing import List

import pytest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if i == len(s) or s[i] != c:
                    return strs[0][:i]

        return strs[0]


@pytest.mark.parametrize(
    ("strs", "expected"),
    [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], "")],
)
def test_longestCommonPrefix(strs: List[str], expected: str):
    assert Solution().longestCommonPrefix(strs) == expected
