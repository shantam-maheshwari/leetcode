from typing import List, Optional

import pytest

from utils.binary_tree import TreeNode, get_binary_tree_from_list


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        else:
            return (
                self.rangeSumBST(root.left, low, high)
                + root.val
                + self.rangeSumBST(root.right, low, high)
            )


@pytest.mark.parametrize(
    ("vals", "low", "high", "expected"),
    [
        ([10, 5, 15, 3, 7, None, 18], 7, 15, 32),
        ([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23),
    ],
)
def test_rangeSumBST(vals: List[Optional[int]], low: int, high: int, expected: int):
    assert (
        Solution().rangeSumBST(get_binary_tree_from_list(vals), low, high) == expected
    )
