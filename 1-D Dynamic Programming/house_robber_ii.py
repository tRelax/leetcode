from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # check the max of a list without first element and a list without last element because of neighbours
        # for case that length of nums is just one number we also take only first number
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        one, two = 0, 0
        for n in nums:
            tmp = max(one + n, two)
            one = two
            two = tmp
        return two


nums = [3, 4, 3]
Solution().rob(nums)
nums = [2, 9, 8, 3, 6]
Solution().rob(nums)
