from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointsHeap = []

        for x, y in points:
            distance = (x**2 + y**2)**0.5
            pointsHeap.append([distance, x, y])

        heapq.heapify(pointsHeap)
        res = []

        while k > 0:
            dist, x, y = heapq.heappop(pointsHeap)
            res.append([x, y])
            k -= 1

        return res


points = [[0, 2], [2, 2]]
k = 1
print(Solution().kClosest(points, k))

points = [[0, 2], [2, 0], [2, 2]]
k = 2
print(Solution().kClosest(points, k))
