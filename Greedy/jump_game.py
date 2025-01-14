from typing import List


class Solution:
    # Greedy
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0

    # DP
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i, min(i + nums[i] + 1, len(nums))):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]


nums = [1, 2, 0, 1, 0]
print(Solution().canJump(nums))
nums = [1, 2, 1, 0, 1]
print(Solution().canJump(nums))
