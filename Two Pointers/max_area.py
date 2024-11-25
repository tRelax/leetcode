from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        cur_max = 0
        while r > 0:
            bigger_stick = min(heights[l], heights[r])
            distance = r - l
            cur_max = max(cur_max, bigger_stick*distance)
            l += 1
            if l == r:
                l = 0
                r -= 1
        return cur_max


sol = Solution()
height = [1, 7, 2, 5, 4, 7, 3, 6]
height = [2, 2, 2]
height = [1, 2]
print(sol.maxArea(height))
