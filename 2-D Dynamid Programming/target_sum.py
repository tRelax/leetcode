from typing import List
from collections import defaultdict


class Solution:
    # top down O(m*n)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = dfs(i+1, total + nums[i]) + \
                dfs(i+1, total - nums[i])
            return dp[(i, total)]

        return dfs(0, 0)

    # space optmized O(n)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            nextDP = defaultdict(int)
            for total, count in dp.items():
                nextDP[total + num] += count
                nextDP[total - num] += count
            dp = nextDP

        return dp[target]


nums = [2, 2, 2]
target = 2

print(Solution().findTargetSumWays(nums, target))
