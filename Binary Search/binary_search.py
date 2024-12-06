from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = l + ((h - l) // 2)

            if nums[mid] > target:
                h = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1


print(Solution().search([-1, 0, 2, 4, 6, 8], 4))
