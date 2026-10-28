from typing import List

import pytest


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])

        [i, j] = click

        if board[i][j] not in "ME":
            return board

        if board[i][j] == "M":
            board[i][j] = "X"
            return board

        next_steps = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
        ]
        mines = 0
        for step in next_steps:
            i1 = i + step[0]
            j1 = j + step[1]

            if 0 <= i1 < m and 0 <= j1 < n and board[i1][j1] == "M":
                mines += 1

        if mines == 0:
            board[i][j] = "B"

            for step in next_steps:
                i1 = i + step[0]
                j1 = j + step[1]

                if 0 <= i1 < m and 0 <= j1 < n:
                    self.updateBoard(board, [i1, j1])
        else:
            board[i][j] = str(mines)

        return board


@pytest.mark.parametrize(
    ("board", "click", "expected"),
    [
        (
            [
                ["E", "E", "E", "E", "E"],
                ["E", "E", "M", "E", "E"],
                ["E", "E", "E", "E", "E"],
                ["E", "E", "E", "E", "E"],
            ],
            [3, 0],
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "M", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
        ),
        (
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "M", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
            [1, 2],
            [
                ["B", "1", "E", "1", "B"],
                ["B", "1", "X", "1", "B"],
                ["B", "1", "1", "1", "B"],
                ["B", "B", "B", "B", "B"],
            ],
        ),
    ],
)
def test_updateBoard(
    board: List[List[str]], click: List[int], expected: List[List[str]]
):
    assert Solution().updateBoard(board, click) == expected
