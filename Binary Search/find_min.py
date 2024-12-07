from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break

            mid = (r + l) // 2

            res = min(nums[mid], res)

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return res


print(Solution().findMin([3, 4, 5, 6, 1, 2]))
