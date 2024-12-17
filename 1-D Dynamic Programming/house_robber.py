from typing import List


class Solution:
    # my solution
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums) - 1, -1, -1):
            two = nums[i+2] if i+2 < len(nums) else 0
            three = nums[i+3] if i+3 < len(nums) else 0
            nums[i] += max(two, three)

        return (max(nums[0], nums[1]))

    # simpler, cleaner
    def rob(self, nums: List[int]) -> int:
        house1, house2 = 0, 0

        # [house1, house2, nums...]
        # -> [house1, nums[0](house2), nums[1], nums[1:]]
        for n in nums:
            tmp = max(house1 + n, house2)
            house1 = house2
            house2 = tmp
        return house2


nums = [2, 9, 8, 3, 6]  # 0 0
print(Solution().rob(nums))
nums = [1, 1, 3, 3]
print(Solution().rob(nums))
nums = [1, 2, 3, 1]
print(Solution().rob(nums))
nums = [5, 1, 2, 10, 6, 2, 7, 9, 3, 1]
print(Solution().rob(nums))
