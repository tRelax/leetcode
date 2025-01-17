from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i] + dp[i - 1])
        return max(dp)

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]

        dp[n-1][1] = dp[n-1][0] = nums[n-1]

        for i in range(n-2, -1, -1):
            dp[i][0] = max(nums[i], dp[i+1][0] + nums[i])
            dp[i][1] = max(dp[i+1][0], dp[i+1][1], dp[i][0])

        return dp[0][1]

    # Kadane's algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curSum = 0
        for num in nums:
            curSum = max(num, curSum + num)
            max_sum = max(max_sum, curSum)

        return max_sum


nums = [2, -3, 4, -2, 2, 1, -1, 4]
print(Solution().maxSubArray(nums))
