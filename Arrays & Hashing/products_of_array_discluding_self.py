from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i != j:
                    prod *= nums[j]
            products.append(prod)

        return products


nums = [1, 2, 4, 6]

sol = Solution()

pr = sol.productExceptSelf(nums)
print(pr)
