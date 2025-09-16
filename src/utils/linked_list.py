from __future__ import annotations

from typing import List, Optional

import pytest


class ListNode:
    def __init__(self, val: int, next: Optional[ListNode] = None):
        self.val = val
        self.next = next


def get_linked_list_from_list(vals: List) -> Optional[ListNode]:
    head = None
    for val in reversed(vals):
        new_node = ListNode(val, head)
        head = new_node
    return head


def get_list_from_linked_list(head: Optional[ListNode]) -> List:
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals


@pytest.mark.parametrize(
    "vals",
    [
        ([]),
        ([1]),
        ([1, 1]),
        ([1, 2, 3]),
    ],
)
def test_get_linked_list_from_list(vals: List):
    expected = vals
    assert get_list_from_linked_list(get_linked_list_from_list(vals)) == expected
