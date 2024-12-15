from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subs = []
        nums.sort()

        def backtrack(i):
            if i >= len(nums):
                res.append(subs.copy())
                return

            subs.append(nums[i])
            backtrack(i+1)
            subs.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i+1)
        backtrack(0)
        return res


Solution().subsetsWithDup([7, 7])
Solution().subsetsWithDup([4, 4, 4, 1, 4])
