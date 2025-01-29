from typing import List
from collections import defaultdict
import heapq


class Solution:
    # n  - number of elements
    # src - starting node
    # dst - destination node
    # k - number of allowed jumps
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for source, dest, cost in flights:
            adjList[source].append((dest, cost))

        minHeap = [(0, 0, src)]  # time, cost, node
        visited = set()
        curPrice = 1000000

        while minHeap:
            t1, c1, n1 = heapq.heappop(minHeap)

            if n1 == dst and t1 <= k:
                curPrice = min(curPrice, c1)
                continue

            if n1 in visited:
                continue

            visited.add(n1)

            if n1 != src:
                t1 += 1

            for n2, c2 in adjList[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, ((t1, c1 + c2, n2)))

        return curPrice if curPrice != 1000000 else -1


n = 3
flights = [[1, 0, 100], [1, 2, 200], [0, 2, 100]]
src = 1
dst = 2
k = 1

print(Solution().findCheapestPrice(n, flights, src, dst, k))

n = 4
flights = [[0, 1, 200], [1, 2, 100], [1, 3, 300], [2, 3, 100]]
src = 0
dst = 3
k = 1
print(Solution().findCheapestPrice(n, flights, src, dst, k))
