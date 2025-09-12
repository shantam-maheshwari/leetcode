from collections import defaultdict, deque
from typing import List, Optional

import pytest

from src.utils.binary_tree import TreeNode, get_binary_tree_from_list


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append((root, 0))
        vertical_levels = defaultdict(list)

        while queue:
            node, col = queue.popleft()

            vertical_levels[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        result = []
        for col in sorted(vertical_levels.keys()):
            result.append(vertical_levels[col])

        return result


@pytest.mark.parametrize(
    ("vals", "expected"),
    [
        ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),
        ([3, 9, 8, 4, 0, 1, 7], [[4], [9], [3, 0, 1], [8], [7]]),
    ],
)
def test_verticalOrder(vals: List[Optional[int]], expected: List[List[int]]):
    assert Solution().verticalOrder(get_binary_tree_from_list(vals)) == expected


# See follow up
# 987. Vertical Order Traversal of a Binary Tree
# where nodes at the same row and col should be sorted by their val
