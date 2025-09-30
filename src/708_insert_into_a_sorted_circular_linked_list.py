from typing import Optional

from src.utils.linked_list import ListNode as Node


class Solution:
    def insert(self, head: Optional[Node], insertVal: int) -> Node:
        if not head:
            head = Node(insertVal)
            head.next = head
            return head

        prev = head
        curr = head.next

        while curr != head:
            if (prev.val <= insertVal <= curr.val) or (
                prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val)
            ):
                new_node = Node(insertVal)
                prev.next = new_node
                new_node.next = curr
                return head

            prev, curr = curr, curr.next

        new_node = Node(insertVal)
        prev.next = new_node
        new_node.next = curr
        return head
