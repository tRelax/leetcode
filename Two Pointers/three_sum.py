from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        l, m, r = 0, 1, len(nums) - 1

        while r > 1:
            cur_sum = nums[l] + nums[m] + nums[r]
            if cur_sum == 0:
                temp_list = [nums[l], nums[m], nums[r]]
                temp_list.sort()
                if not temp_list in sums:
                    sums.append(temp_list)

            m += 1
            if m == r:
                l += 1
                m = l+1

            if l+1 == r:
                l = 0
                m = 1
                r -= 1

        return sums


sol = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(sol.threeSum(nums))
