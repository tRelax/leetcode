from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        biggest_seq = 0
        curr_num, curr_seq = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] - curr_num == 1:
                curr_seq += 1
                if i == len(nums) - 1:
                    biggest_seq = max(biggest_seq, curr_seq)
            else:
                biggest_seq = max(biggest_seq, curr_seq)
                curr_seq = 1

            curr_num = nums[i]

        return biggest_seq


sol = Solution()

nums1 = [2, 20, 4, 10, 3, 4, 5]
# 4
nums2 = [0, 3, 2, 5, 4, 6, 1, 1]
# 7
nums3 = [1, 2, 3, 5, 6, 7, 8, 9]


print(sol.longestConsecutive(nums2))
