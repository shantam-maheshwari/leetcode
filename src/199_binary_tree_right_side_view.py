from collections import deque
from typing import List, Optional

import pytest

from src.utils.binary_tree import TreeNode, get_binary_tree_from_list


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return result

        queue = deque()
        queue.append(root)

        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.popleft()

                if i == queue_len - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


@pytest.mark.parametrize(
    ("vals", "expected"),
    [
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5]),
        ([1, None, 3], [1, 3]),
        ([], []),
    ],
)
def test_rightSideView(vals: List[Optional[int]], expected: List[int]):
    assert Solution().rightSideView(get_binary_tree_from_list(vals)) == expected
