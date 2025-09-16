from typing import List

import pytest


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_times = [0] * n
        stack = []
        prev_time = 0

        for i, log in enumerate(logs):
            [fn, state, time] = log.split(":")
            fn, time = int(fn), int(time)

            if state == "start":
                if stack:
                    exclusive_times[stack[-1]] += time - prev_time
                stack.append(fn)
                prev_time = time
            else:
                exclusive_times[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return exclusive_times


@pytest.mark.parametrize(
    ("n", "logs", "expected"),
    [
        (2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"], [3, 4]),
        (
            1,
            ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"],
            [8],
        ),
        (
            2,
            ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"],
            [7, 1],
        ),
    ],
)
def test_exclusiveTime(n: int, logs: List[str], expected: List[int]):
    assert Solution().exclusiveTime(n, logs) == expected
