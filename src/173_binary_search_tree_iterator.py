from typing import Optional

from src.utils.binary_tree import TreeNode, get_binary_tree_from_list


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        result = node.val

        if node.right:
            node = node.right

            while node:
                self.stack.append(node)
                node = node.left

        return result

    def hasNext(self) -> bool:
        return len(self.stack) > 0


def test_BSTIterator():
    root = get_binary_tree_from_list([7, 3, 15, None, None, 9, 20])
    it = BSTIterator(root)
    assert it.next() == 3
    assert it.next() == 7
    assert it.hasNext()
    assert it.next() == 9
    assert it.hasNext()
    assert it.next() == 15
    assert it.hasNext()
    assert it.next() == 20
    assert not it.hasNext()
