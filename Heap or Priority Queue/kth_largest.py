from typing import List
import heapq


class KthLargest:
    # using sorting
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]

    # using min heap
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        if val > self.minHeap[0]:
            heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


kth = KthLargest(3, [1, 2, 3, 3])
print(kth.add(3))   # return 3
print(kth.add(5))   # return 3
print(kth.add(6))   # return 3
print(kth.add(7))   # return 5
print(kth.add(8))   # return 6
