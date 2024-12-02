from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, k
        while r <= len(nums):
            window = nums[l:r]
            print(window)
            res.append(max(window))
            l+=1
            r+=1
        return res

nums = [1,2,1,0,4,2,6]
k = 3
print(Solution().maxSlidingWindow(nums, k))