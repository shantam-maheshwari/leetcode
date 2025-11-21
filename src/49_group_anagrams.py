from collections import defaultdict
from typing import List

import pytest


# O(N*L) where N: num of strings, L: max length of a string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups[self.char_count(s)].append(s)
        return list(groups.values())

    def char_count(self, s: str):
        letters = [0] * 26
        for c in s:
            letters[ord(c) - ord("a")] += 1
        return tuple(letters)


@pytest.mark.parametrize(
    ("strs", "expected"),
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_groupAnagrams(strs: List[str], expected: List[List[str]]):
    result = sorted([sorted(x) for x in Solution().groupAnagrams(strs)])
    expected = sorted([sorted(x) for x in expected])
    assert result == expected
