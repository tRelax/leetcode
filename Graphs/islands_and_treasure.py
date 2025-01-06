from typing import List
from collections import deque


class Solution:
    # backtracking
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1 or visited[r][c]:
                return INF
            if grid[r][c] == 0:
                return 0

            visited[r][c] = True
            res = INF
            for dr, dc in directions:
                res = min(res, 1 + dfs(r + dr, c + dc))
            visited[r][c] = False
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = dfs(r, c)
        return grid

    # bfs
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        INF = 2147483647

        def bfs(r, c):
            q = deque([(r, c)])
            visit = [[False] * COLS for _ in range(ROWS)]
            visit[r][c] = True
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and not visit[nr][nc] and grid[nr][nc] != -1:
                            q.append((nr, nc))
                            visit[nr][nc] = True
                steps += 1
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)

        print(grid)

    # multi bfs
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        steps = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = steps
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit and grid[nr][nc] != -1:
                        q.append((nr, nc))
                        visit.add((nr, nc))
            steps += 1

        print(grid)


# -1 - A water cell that can not be traversed.
# 0 - A treasure chest.
# INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
grid = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]
Solution().islandsAndTreasure(grid)
grid = [
    [0, -1],
    [2147483647, 2147483647]
]
Solution().islandsAndTreasure(grid)
