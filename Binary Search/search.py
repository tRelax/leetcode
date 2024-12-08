from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2

            if nums[m] == target:
                return m
            # left sorted portion
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1


# 2341

# 5 1 3
print(Solution().search(nums=[3, 4, 5, 6, 1, 2], target=1))
print(Solution().search(nums=[3, 5, 6, 0, 1, 2], target=4))
print(Solution().search(nums=[1, 3], target=3))
