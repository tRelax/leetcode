from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]


nums = [2, 3, 1, 5, 4]
k = 2
Solution().findKthLargest(nums, k)
nums = [2, 3, 1, 1, 5, 5, 4]
k = 3
Solution().findKthLargest(nums, k)
nums = [-1, -1]
k = 2
Solution().findKthLargest(nums, k)
