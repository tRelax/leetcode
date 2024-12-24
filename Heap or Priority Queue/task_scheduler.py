from typing import List
from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        q = deque()  # [count, timeToReEnter]
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


tasks = ["X", "X", "Y", "Y"]
n = 2
print(Solution().leastInterval(tasks, n))
tasks = ["A", "A", "A", "B", "C"]
n = 3
print(Solution().leastInterval(tasks, n))
