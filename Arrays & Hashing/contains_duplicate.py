
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                return True
        return False

# Input: nums = [1, 2, 3, 3]
# Output: true
