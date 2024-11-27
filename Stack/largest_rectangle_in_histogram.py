from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0

        for i in range(len(heights)):
            stack = []
            stack.append(heights[i])
            min_size = min(stack)
            area = min_size * (len(stack))
            largest_area = max(largest_area, area)

            for j in range(i+1, len(heights)):
                stack.append(heights[j])
                min_size = min(stack)
                area = min_size * (len(stack))
                largest_area = max(largest_area, area)

        return largest_area


heights = [7, 1, 7, 2, 2, 4]
# heights = [1, 3, 7]
print(Solution().largestRectangleArea(heights))
