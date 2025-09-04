from typing import Optional

from src.utils.binary_tree import TreeNode


class Solution:
    diameter = float("-inf")

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.diameter

    def dfs(self, node: Optional[TreeNode]) -> int:
        """returns longest path rooted at node"""
        if not node:
            return 0

        left_path = self.dfs(node.left)
        right_path = self.dfs(node.right)
        self.diameter = max(self.diameter, left_path + right_path)

        return max(left_path, right_path) + 1
