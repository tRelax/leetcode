class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(cur_sum):
            if cur_sum >= n:
                return cur_sum == n
            return dfs(cur_sum + 1) + dfs(cur_sum + 2)

        return dfs(0)

    # 1d dp solution
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp

        return one


print(Solution().climbStairs(5))
