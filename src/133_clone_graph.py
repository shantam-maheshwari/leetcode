from collections import deque
from typing import Optional

from src.utils.graph import GraphNode

Node = GraphNode


class Solution:
    # # recursive
    # old_to_new_map = {}

    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     if not node:
    #         return None

    #     if node in self.old_to_new_map:
    #         return self.old_to_new_map[node]

    #     new_node = Node(node.val)
    #     self.old_to_new_map[node] = new_node

    #     for neighbor in node.neighbors:
    #         new_node.neighbors.append(self.cloneGraph(neighbor))

    #     return new_node

    # iterative
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        old_to_new_map = {}

        queue = deque()
        queue.append(node)

        new_node = Node(node.val)
        old_to_new_map[node] = new_node

        while queue:
            old_node = queue.popleft()

            for neighbor in old_node.neighbors:
                if neighbor not in old_to_new_map:
                    old_to_new_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new_map[old_node].neighbors.append(old_to_new_map[neighbor])

        return new_node
