from typing import List

import pytest

from src.utils.linked_list import (
    ListNode,
    get_linked_list_from_list,
    get_list_from_linked_list,
)

# # O(n)
# class Solution:
#     def deleteNode(self, node):
#        prev = None
#        curr = node
#        while curr.next:
#            next = curr.next
#            curr.val = next.val

#            prev = curr
#            curr = next

#        prev.next = None


# O(1)
class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next


@pytest.mark.parametrize(
    ("vals", "node_idx", "expected"),
    [([4, 5, 1, 9], 1, [4, 1, 9]), ([4, 5, 1, 9], 2, [4, 5, 9])],
)
def test_deleteNode(vals: List[int], node_idx: int, expected: List[int]):
    ll = get_linked_list_from_list(vals)

    curr = ll
    for _ in range(node_idx):
        curr = curr.next

    Solution().deleteNode(curr)

    assert get_list_from_linked_list(ll) == expected
