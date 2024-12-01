from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            cur_price = prices[i]
            after_prices = prices[i:]
            max_price = max(after_prices)
            max_profit = max(max_profit, max_price - cur_price)
        return max_profit


prices = [10, 1, 5, 6, 7, 1]
print(Solution().maxProfit(prices))
