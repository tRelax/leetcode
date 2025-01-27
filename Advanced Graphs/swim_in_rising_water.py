from typing import List
import heapq


class Solution:
    # Dijkstra's Algorithm
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [(grid[0][0], 0, 0)]  # (time, x, y)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visit.add((0, 0))
        while minHeap:
            t, x, y = heapq.heappop(minHeap)

            if x == y == N - 1:
                return t

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx < 0 or ny < 0 or nx == N or ny == N or (nx, ny) in visit:
                    continue

                visit.add((nx, ny))
                heapq.heappush(minHeap, (max(t, grid[nx][ny]), nx, ny))


grid = [[0, 1], [2, 3]]
print(Solution().swimInWater(grid))

grid = [
    [0, 1, 2, 10],
    [9, 14, 4, 13],
    [12, 3, 8, 15],
    [11, 5, 7, 6]
]
print(Solution().swimInWater(grid))
