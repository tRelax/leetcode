import heapq


class MedianFinder:

    def __init__(self):
        self.smallHeap = []  # max heap
        self.bigHeap = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -num)

        if self.smallHeap and self.bigHeap and -self.smallHeap[0] > self.bigHeap[0]:
            heapq.heappush(self.bigHeap, -heapq.heappop(self.smallHeap))

        if len(self.smallHeap) > len(self.bigHeap) + 1:
            heapq.heappush(self.bigHeap, -heapq.heappop(self.smallHeap))

        if len(self.bigHeap) > len(self.smallHeap) + 1:
            heapq.heappush(self.smallHeap, -heapq.heappop(self.bigHeap))

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.bigHeap):
            return -self.smallHeap[0]
        elif len(self.smallHeap) < len(self.bigHeap):
            return self.bigHeap[0]
        return (-self.smallHeap[0] + self.bigHeap[0]) / 2


medianFinder = MedianFinder()
medianFinder.addNum(1)    # arr = [1]
print(medianFinder.findMedian())  # return 1.0
medianFinder.addNum(3)    # arr = [1, 3]
print(medianFinder.findMedian())  # return 2.0
medianFinder.addNum(2)    # arr[1, 2, 3]
print(medianFinder.findMedian())  # return 2.0
