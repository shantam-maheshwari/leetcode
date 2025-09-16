from typing import List, Optional, Tuple

import pytest

from src.utils.binary_tree import TreeNode, get_binary_tree_from_list


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        return self.dfs(root)[0]

    # (result, sum, size)
    def dfs(self, node: Optional[TreeNode]) -> Tuple[int, int, int]:
        if not node:
            return (0, 0, 0)

        left_result, left_sum, left_size = self.dfs(node.left)
        right_result, right_sum, right_size = self.dfs(node.right)

        sum = left_sum + node.val + right_sum
        size = left_size + 1 + right_size
        result = left_result + (node.val == sum // size) + right_result

        return (result, sum, size)


@pytest.mark.parametrize(
    ("vals", "expected"), [([4, 8, 5, 0, 1, None, 6], 5), ([1], 1)]
)
def test_averageOfSubtree(vals: List[Optional[int]], expected: int):
    assert Solution().averageOfSubtree(get_binary_tree_from_list(vals)) == expected
