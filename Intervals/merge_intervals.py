from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res


intervals = [[1, 3], [6, 7], [1, 5]]
print(Solution().merge(intervals))  # [[1, 5], [6, 7]]
intervals = [[1, 2], [2, 3]]
print(Solution().merge(intervals))  # [[1, 3]]
