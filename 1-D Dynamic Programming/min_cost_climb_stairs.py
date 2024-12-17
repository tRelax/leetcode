from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[-2]
        two = cost[-1]

        for i in range(1, len(cost) - 2):
            x = len(cost) - 2 - i
            tmp = one
            one = min(one, two) + cost[x]
            two = tmp
        one = min(one, two+cost[0])
        return one


Solution().minCostClimbingStairs(cost=[1, 2, 3])
Solution().minCostClimbingStairs(cost=[1, 2, 1, 2, 1, 1, 1])
