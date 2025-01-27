from typing import List
from collections import defaultdict
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = defaultdict(list)
        n = len(points)

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        for i in range(n):
            for j in range(i + 1, n):
                edges[i].append((j, dist(points[i], points[j])))
                edges[j].append((i, dist(points[i], points[j])))

        minHeap = [(0, 0)]
        visited = set()
        res = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue

            visited.add(n1)
            res += w1

            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w2, n2))

        return res


points = [[0, 0], [2, 2], [3, 3], [2, 4], [4, 2]]
print(Solution().minCostConnectPoints(points))  # 10
