from collections import deque
from typing import List


class Solution:
    # 0: empty cell
    # 1: fresh orange
    # 2: rotten orange
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()
        visited = set()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        fresh -= 1
            minutes += 1

        return max(0, minutes - 1) if fresh == 0 else -1


grid = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 1, 2]
]
print(Solution().orangesRotting(grid))  # 4
