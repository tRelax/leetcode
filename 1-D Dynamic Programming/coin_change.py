from typing import List


class Solution:
    # top-down
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount-coin))
            memo[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins >= 1e9 else minCoins

    # bottom-up
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount+1] * (amount + 1)
        memo[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    memo[a] = min(memo[a], 1 + memo[a-c])

        return memo[amount] if memo[amount] != (amount + 1) else -1


print(Solution().coinChange([1, 5, 10], 12))
