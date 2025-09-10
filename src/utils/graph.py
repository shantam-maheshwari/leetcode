from collections import deque
from typing import Dict, List, Optional, Set, Tuple, TypeAlias

import pytest


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors: List[GraphNode] = []


Edge: TypeAlias = Tuple[int, int]


def get_graph_from_edges(edges: Set[Edge]) -> Optional[GraphNode]:
    if not edges:
        return None

    val_to_node_map: Dict[int, GraphNode] = {}

    def get_or_create_node(val: int) -> GraphNode:
        if val not in val_to_node_map:
            val_to_node_map[val] = GraphNode(val)

        return val_to_node_map[val]

    for edge in edges:
        u, v = edge
        node_u = get_or_create_node(u)
        node_v = get_or_create_node(v)

        node_u.neighbors.append(node_v)
        node_v.neighbors.append(node_u)

    first_node_val = next(iter(val_to_node_map))

    return val_to_node_map[first_node_val]


def get_edges_from_graph(node: GraphNode) -> Set[Edge]:
    visited: Set[GraphNode] = set()
    edges: Set[Edge] = set()

    queue = deque([node])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)

            for neighbor in node.neighbors:
                edge = tuple(sorted([node.val, neighbor.val]))
                edges.add(edge)
                queue.append(neighbor)

    return edges


@pytest.mark.parametrize(("edges"), [([[0, 1], [1, 2], [0, 2], [2, 3]])])
def test_get_graph_from_edges(edges: List[List[int]]):
    expected = set([(u, v) for [u, v] in edges])
    assert get_edges_from_graph(get_graph_from_edges(edges)) == expected
