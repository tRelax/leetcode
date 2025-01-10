from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda x: x[1])
        end = float('-inf')

        for interval in intervals:
            if interval[0] >= end:
                end = interval[1]
            else:
                res += 1

        return res


intervals = [[1, 2], [2, 4], [1, 4]]
print(Solution().eraseOverlapIntervals(intervals))  # 1
