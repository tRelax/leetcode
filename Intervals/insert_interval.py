from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1])
            ]
            i += 1

        result.append(newInterval)

        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result


intervals = [[1, 3], [4, 6]]
newInterval = [2, 5]

Solution().insert(intervals, newInterval)
