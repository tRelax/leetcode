from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def capt(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return

            board[r][c] = "T"
            for dr, dc in directions:
                capt(r+dr, c+dc)

        for r in range(ROWS):
            if board[r][0] == "O":
                capt(r, 0)
            if board[r][COLS-1] == "O":
                capt(r, COLS-1)

        for c in range(COLS):
            if board[0][c] == "O":
                capt(0, c)
            if board[ROWS-1][c] == "O":
                capt(ROWS-1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

        print(board)


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "X", "O"]
]

Solution().solve(board)
# [
#  ["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","X","X","O"]
# ]
