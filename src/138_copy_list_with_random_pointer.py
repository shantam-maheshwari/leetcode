from typing import Optional, Self


class Node:
    def __init__(self, x: int, next: Self = None, random: Self = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # recursive
    old_to_new_map = {}

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        if head in self.old_to_new_map:
            return self.old_to_new_map[head]

        new_head = Node(head.val)
        self.old_to_new_map[head] = new_head
        new_head.next = self.copyRandomList(head.next)
        new_head.random = self.copyRandomList(head.random)

        return new_head

    # # iterative
    # old_to_new_map = {}

    # def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
    #     if not head:
    #         return None

    #     new_head = Node(head.val)

    #     self.old_to_new_map[head] = new_head

    #     old_node = head
    #     new_node = new_head
    #     while old_node:
    #         new_node.next = self.getClonedNode(old_node.next)
    #         new_node.random = self.getClonedNode(old_node.random)

    #         old_node = old_node.next
    #         new_node = new_node.next

    #     return new_head

    # def getClonedNode(self, head: Optional[Node]) -> Optional[Node]:
    #     if not head:
    #         return None

    #     if head in self.old_to_new_map:
    #         return self.old_to_new_map[head]

    #     new_head = Node(head.val)
    #     self.old_to_new_map[head] = new_head

    #     return new_head
