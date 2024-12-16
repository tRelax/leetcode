class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(cur_sum):
            if cur_sum >= n:
                return cur_sum == n
            return dfs(cur_sum + 1) + dfs(cur_sum + 2)

        return dfs(0)


print(Solution().climbStairs(3))
