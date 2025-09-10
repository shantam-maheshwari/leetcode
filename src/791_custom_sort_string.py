import pytest


class Solution:
    # # m = len(order)
    # # n = len(s)
    # # time complexity: O(m + n*log(n))
    # def customSortString(self, order: str, s: str) -> str:
    #     pos = {c: i for i, c in enumerate(order)}
    #     result = sorted(s, key=lambda x: pos.get(x, -1))
    #     return "".join(result)

    # m = len(order)
    # n = len(s)
    # time complexity: O(n + m)
    def customSortString(self, order: str, s: str) -> str:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord("a")] += 1

        result = ""
        for c in order:
            result += c * counts[ord(c) - ord("a")]
            counts[ord(c) - ord("a")] = 0

        for i, count in enumerate(counts):
            if count:
                c = chr(i + ord("a"))
                result += c * count

        return result


@pytest.mark.parametrize(
    ("order", "s", "expected"),
    [
        ("cba", "abcd", ["cbad", "dcba", "cdba", "cbda"]),
    ],
)
def test_customSortString(order: str, s: str, expected: str):
    assert Solution().customSortString(order, s) in set(expected)
