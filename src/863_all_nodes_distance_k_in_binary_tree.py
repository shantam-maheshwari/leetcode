from collections import defaultdict, deque
from typing import List

from src.utils.binary_tree import TreeNode, get_binary_tree_from_list


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        # create graph
        graph = defaultdict(list)
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                queue.append(node.right)
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)

        # bfs
        distance = 0
        queue.append(target.val)
        visited = set([target.val])
        while queue:
            if distance == k:
                return list(queue)

            for _ in range(len(queue)):
                node = queue.popleft()

                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append(neighbour)
            distance += 1

        return []


def test_distanceK():
    vals = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root = get_binary_tree_from_list(vals)
    target = root.left
    assert set(Solution().distanceK(root, target, 2)) == set([7, 4, 1])
