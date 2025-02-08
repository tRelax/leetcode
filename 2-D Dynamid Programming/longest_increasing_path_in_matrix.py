from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}  # (i,j): LIP
        ROWS, COLS = len(matrix), len(matrix[0])
        # up, down, left, right
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j, prevVal):
            if i < 0 or i == ROWS or j < 0 or j == COLS or matrix[i][j] <= prevVal:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            for di, dj in directions:
                res = max(res, 1 + dfs(i+di, j+dj, matrix[i][j]))

            dp[(i, j)] = res
            return res

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, -1)
        return max(dp.values())


matrix = [
    [5, 5, 3],
    [2, 3, 6],
    [1, 1, 1]
]
print(Solution().longestIncreasingPath(matrix))
matrix = [
    [1, 2, 3],
    [2, 1, 4],
    [7, 6, 5]
]
print(Solution().longestIncreasingPath(matrix))
