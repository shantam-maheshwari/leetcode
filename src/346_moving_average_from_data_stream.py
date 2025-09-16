from collections import deque

import pytest


class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum += val

        if len(self.queue) > self.size:
            self.sum -= self.queue.popleft()

        return self.sum / len(self.queue)


def test_MovingAverage():
    obj = MovingAverage(3)
    assert obj.next(1) == 1.0
    assert obj.next(10) == 5.5
    assert obj.next(3) == pytest.approx(4.666667)
    assert obj.next(5) == 6.0
