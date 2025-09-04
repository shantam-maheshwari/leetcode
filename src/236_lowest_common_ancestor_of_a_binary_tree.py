from typing import Optional

from src.utils.binary_tree import TreeNode


class Solution:
    lca: Optional[TreeNode] = None

    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        self.dfs(root, p, q)
        return self.lca

    def dfs(self, node: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        """returns whether node contains p or q"""
        if not node:
            return False

        node_is_p_or_q = node == p or node == q
        left_contains_p_or_q = self.dfs(node.left, p, q)
        right_contains_p_or_q = self.dfs(node.right, p, q)

        if node_is_p_or_q + left_contains_p_or_q + right_contains_p_or_q == 2:
            self.lca = node

        return node_is_p_or_q or left_contains_p_or_q or right_contains_p_or_q
