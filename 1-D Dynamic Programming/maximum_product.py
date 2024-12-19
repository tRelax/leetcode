from typing import List


class Solution:
    # brute force
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")

        # 1,2,4,-1
        for i in range(len(nums)):
            cur_prod = nums[i]
            res = max(res, cur_prod)
            for j in range(i+1, len(nums)):
                cur_prod *= nums[j]
                res = max(res, cur_prod)
        return res

    # dp
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            tmp = curMax
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp * n, curMin * n, n)
            res = max(res, curMax, curMin)

        return res


print(Solution().maxProduct(nums=[1, 2, -3, 4]))
print(Solution().maxProduct(nums=[-2, -1]))
