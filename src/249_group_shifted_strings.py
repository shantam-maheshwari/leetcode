from collections import defaultdict
from typing import List

import pytest


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strings:
            key = tuple([(ord(c) - ord(s[0])) % 26 for c in s])
            map[key].append(s)

        return list(map.values())


@pytest.mark.parametrize(
    ("strings", "expected"),
    [
        (
            ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
            [["acef"], ["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"]],
        ),
        (["a"], [["a"]]),
    ],
)
def test_groupStrings(strings: List[str], expected: List[List[str]]):
    result = Solution().groupStrings(strings)
    result = set([tuple(s) for s in result])

    expected = set([tuple(s) for s in expected])

    assert result == expected
