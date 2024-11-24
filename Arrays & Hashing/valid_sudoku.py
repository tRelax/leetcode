from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        # col
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        # box
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j

                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True


sol = Solution()

example1 = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# expected True

example2 = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
            ["4", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", "9", "1", ".", ".", ".", ".", ".", "3"],
            ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
            [".", ".", ".", "8", ".", "3", ".", ".", "5"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", "2", ".", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "8"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# expected False

example3 = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["5", ".", ".", ".", ".", ".", ".", "9", "."],
            [".", ".", ".", "5", "6", ".", ".", ".", "."],
            ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
            [".", ".", ".", "7", ".", ".", ".", ".", "."],
            [".", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]]

s = sol.isValidSudoku(example2)
print(s)
