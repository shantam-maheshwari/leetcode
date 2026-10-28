from typing import List

import pytest


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        time_spent = [0] * n
        stack = []
        prev_start_time = 0

        for log in logs:
            [id, status, timestamp] = log.split(":")
            id, timestamp = int(id), int(timestamp)

            if not stack:
                stack.append(id)
                continue

            if status == "start":
                prev_id = stack[-1]
                time_spent[prev_id] += timestamp - prev_start_time

                stack.append(id)
                prev_start_time = timestamp
            else:
                prev_id = stack.pop()
                time_spent[prev_id] += timestamp - prev_start_time + 1

                prev_start_time = timestamp + 1

        return time_spent


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
