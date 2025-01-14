from typing import List
from collections import deque


class Solution:
    # DP
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [100000] * n
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            for j in range(i, min(i + nums[i] + 1, n)):
                dp[i] = min(dp[i], dp[j] + 1)

        return dp[0]

    # Greedy
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        steps = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l, r = r + 1, farthest
            steps += 1
        return steps


nums = [2, 4, 1, 1, 1, 1]
print(Solution().jump(nums))  # 2
