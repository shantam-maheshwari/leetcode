class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._create_dll()
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._remove_node(node)
            self._insert_at_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self._remove_node(node)
            self._insert_at_head(node)
        else:
            node = ListNode(key, value)
            self.map[key] = node
            self._insert_at_head(node)

            if len(self.map) > self.capacity:
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.map[lru_node.key]

    def _create_dll(self):
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_at_head(self, node: ListNode):
        next = self.head.next

        self.head.next = node
        node.prev = self.head

        next.prev = node
        node.next = next


def test_LRUCache():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)

    assert lru.get(1) == 1

    lru.put(3, 3)

    assert lru.get(2) == -1

    lru.put(4, 4)

    assert lru.get(1)
    assert lru.get(3)
    assert lru.get(4)
