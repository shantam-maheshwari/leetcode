from collections import deque
from typing import List, Optional

import pytest


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def get_binary_tree_from_list(vals: List[Optional[int]]) -> Optional[TreeNode]:
    def helper(i: int, vals: List[Optional[int]]) -> Optional[TreeNode]:
        if i >= len(vals) or vals[i] is None:
            return None

        node = TreeNode(vals[i])
        node.left = helper(2 * i + 1, vals)
        node.right = helper(2 * i + 2, vals)
        return node

    return helper(0, vals)


def get_list_from_binary_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []

    vals = []
    queue = deque([root])
    while queue:
        node = queue.popleft()

        if node:
            vals.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            vals.append(None)

    while vals and vals[-1] is None:
        vals.pop()

    return vals


@pytest.mark.parametrize(
    ("vals"),
    [
        ([]),
        ([1]),
        ([5, 1, 8, 7, 6, None, 4]),
    ],
)
def test_get_binary_tree_from_list(vals: List[Optional[int]]):
    expected = vals
    assert get_list_from_binary_tree(get_binary_tree_from_list(vals)) == expected
