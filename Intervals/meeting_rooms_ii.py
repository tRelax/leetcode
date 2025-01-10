from typing import List

# Definition of Interval


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([i.start for i in intervals])
        end_times = sorted([i.end for i in intervals])

        start_pointer = end_pointer = 0
        used_rooms = 0

        while start_pointer < len(intervals):
            # if the current start time is greater than or equal to the end time of meeting, then we can reuse the room
            if start_times[start_pointer] >= end_times[end_pointer]:
                used_rooms -= 1
                end_pointer += 1

            used_rooms += 1
            start_pointer += 1

        return used_rooms


intervals = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
# 1 [0, 40] and [[5, 10], [15, 20]]
print(Solution().minMeetingRooms(intervals))
