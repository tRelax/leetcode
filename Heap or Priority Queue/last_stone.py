from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heapq._heapify_max(stones)
            first = heapq.heappop(stones)
            heapq._heapify_max(stones)
            second = heapq.heappop(stones)
            heapq.heappush(stones, first-second)
        return stones[0]

    # same solution just cleaner
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, first-second)
        return abs(maxHeap[0])


stones = [2, 3, 6, 2, 4]
Solution().lastStoneWeight(stones)
stones = [1]
Solution().lastStoneWeight(stones)
