from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subs = []

        def bt(i):
            if i >= len(nums):
                res.append(subs.copy())
                return

            subs.append(nums[i])
            bt(i+1)
            subs.pop()
            bt(i+1)

        bt(0)
        return res


print(Solution().subsets([1, 2, 3]))
# [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
