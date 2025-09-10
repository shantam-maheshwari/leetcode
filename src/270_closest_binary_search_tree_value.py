from typing import List, Optional

import pytest

from src.utils.binary_tree import TreeNode, get_binary_tree_from_list


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest_val = float("inf")

        while root:
            if abs(root.val - target) < abs(closest_val - target):
                closest_val = root.val
            elif (
                abs(root.val - target) == abs(closest_val - target)
                and root.val < closest_val
            ):
                closest_val = root.val
            elif root.val < target:
                root = root.right
            else:
                root = root.left

        return closest_val


@pytest.mark.parametrize(
    ("vals", "target", "expected"),
    [
        ([4, 2, 5, 1, 3], 3.714286, 4),
        ([4, 2, 5, 1, 3], 3.5, 3),
        ([1], 4.428571, 1),
        ([4, 2, 5, 1, 3], 4.5, 4),
    ],
)
def test_closestValue(vals: List[int], target: float, expected: int):
    assert Solution().closestValue(get_binary_tree_from_list(vals), target) == expected
