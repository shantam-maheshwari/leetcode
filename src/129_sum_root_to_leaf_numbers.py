from typing import List, Optional

import pytest

from src.utils.binary_tree import TreeNode, get_binary_tree_from_list


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, root: Optional[TreeNode], num: int) -> int:
        if not root:
            return 0

        num = num * 10 + root.val
        if not root.left and not root.right:
            return num

        return self.dfs(root.left, num) + self.dfs(root.right, num)


@pytest.mark.parametrize(
    ("vals", "expected"), [([1, 2, 3], 25), ([4, 9, 0, 5, 1], 1026)]
)
def test_sumNumbers(vals: List[Optional[int]], expected: int):
    assert Solution().sumNumbers(get_binary_tree_from_list(vals)) == expected
