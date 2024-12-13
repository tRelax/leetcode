from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            # include first number and start again from first number
            cur.append(nums[i])
            dfs(i, total + nums[i])
            # not include first number and go from there
            cur.pop()
            dfs(i+1, total)

        dfs(0, 0)
        return res


print(Solution().combinationSum(nums=[2, 5, 6, 9], target=9))
print(Solution().combinationSum(nums=[3, 4, 5], target=16))
