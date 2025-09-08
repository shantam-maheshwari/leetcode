class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        seen = set()
        curr = p
        while curr:
            seen.add(curr)
            curr = curr.parent

        curr = q
        while curr:
            if curr in seen:
                return curr
            curr = curr.parent

        return None
