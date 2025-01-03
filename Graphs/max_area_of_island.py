from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, curArea):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0

            curArea += 1
            grid[r][c] = 0

            for dr, dc in directions:
                curArea += dfs(r+dr, c+dc, 0)

            return curArea

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c, 0))

        print(maxArea)
        return maxArea


grid = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 0, 1]
]

Solution().maxAreaOfIsland(grid)

grid = [
    [0],
    [0]
]

Solution().maxAreaOfIsland(grid)
