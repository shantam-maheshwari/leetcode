from typing import List

import pytest


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    if i > 0 and board[i - 1][j] == "X":
                        continue
                    if j > 0 and board[i][j - 1] == "X":
                        continue
                    count += 1
        return count


@pytest.mark.parametrize(
    ("board", "expected"),
    [
        ([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]], 2),
        ([["."]], 0),
    ],
)
def test_countBattleships(board: List[List[str]], expected: int):
    assert Solution().countBattleships(board) == expected
