from collections import defaultdict, deque
from typing import List, Optional

import pytest

from src.utils.binary_tree import TreeNode, get_binary_tree_from_list


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = defaultdict(list)

        queue = deque()
        queue.append((root, (0, 0)))
        while queue:
            node, (row, col) = queue.popleft()
            levels[col].append((row, node.val))

            if node.left:
                queue.append((node.left, (row + 1, col - 1)))
            if node.right:
                queue.append((node.right, (row + 1, col + 1)))

        result = []
        for col in sorted(levels.keys()):
            levels[col].sort()
            vals = [pair[1] for pair in levels[col]]
            result.append(vals)
        return result


@pytest.mark.parametrize(
    ("vals", "expected"),
    [
        ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),
        ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]),
        ([1, 2, 3, 4, 6, 5, 7], [[4], [2], [1, 5, 6], [3], [7]]),
    ],
)
def test_verticalTraversal(vals: List[Optional[int]], expected: List[List[int]]):
    assert Solution().verticalTraversal(get_binary_tree_from_list(vals)) == expected
