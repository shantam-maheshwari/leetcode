from typing import List, Optional

import pytest

from src.utils.linked_list import (
    ListNode,
    get_linked_list_from_list,
    get_list_from_linked_list,
)


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode(-1)

        carry = 0
        l3 = result
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            l3.next = ListNode((num1 + num2 + carry) % 10)
            carry = (num1 + num2 + carry) // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            l3 = l3.next

        return result.next


@pytest.mark.parametrize(
    ("vals1", "vals2", "expected"),
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ],
)
def test_addTwoNumbers(vals1: List[int], vals2: List[int], expected: List[int]):
    l1 = get_linked_list_from_list(vals1)
    l2 = get_linked_list_from_list(vals2)
    assert get_list_from_linked_list(Solution().addTwoNumbers(l1, l2)) == expected
