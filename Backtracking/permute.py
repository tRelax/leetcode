from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            for i in range(len(p) + 1):
                pc = p.copy()
                pc.insert(i, nums[0])
                res.append(pc)

        return res


nums = [1, 2, 3]
print(Solution().permute(nums))
