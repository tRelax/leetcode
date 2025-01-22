from collections import defaultdict
import heapq
from typing import List


class Solution:
    # Dijkstra's algorithm
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        # u - source node
        # v - target node
        # w - time needed from source to target node
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            # pop the smallest element from the heap (by time needed to reach the node)
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, n2))
        return t if len(visit) == n else -1


times = [[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]]
n = 4
k = 1

print(Solution().networkDelayTime(times, n, k))  # 3
