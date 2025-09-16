from typing import List, Optional

import pytest

from src.utils.linked_list import (
    ListNode,
    get_linked_list_from_list,
    get_list_from_linked_list,
)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = fast = head
        for _ in range(n):
            fast = fast.next

        if fast is None:
            return slow.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head


@pytest.mark.parametrize(
    ("vals", "n", "expected"),
    [([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]), ([1], 1, []), ([1, 2], 1, [1])],
)
def test_removeNthFromEnd(vals: List[int], n: int, expected: List[int]):
    assert (
        get_list_from_linked_list(
            Solution().removeNthFromEnd(get_linked_list_from_list(vals), n)
        )
        == expected
    )
