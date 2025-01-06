from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        q.append((nr, nc))

                        ocean[nr][nc] = True

        pacific = []
        atlantic = []

        for c in range(COLS):
            pacific.append([0, c])
            atlantic.append([ROWS - 1, c])

        for r in range(ROWS):
            pacific.append([r, 0])
            atlantic.append([r, COLS - 1])

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res


heights = [
    [4, 2, 7, 3, 4],
    [7, 4, 6, 4, 7],
    [6, 3, 5, 3, 6]
]
# [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
print(Solution().pacificAtlantic(heights))

heights = [
    [1],
    [1]
]
# [[0,0],[0,1]]
print(Solution().pacificAtlantic(heights))
