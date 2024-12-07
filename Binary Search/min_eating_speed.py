from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        lowestSpeed = 0
        while low <= high:
            mid = low + ((high-low) // 2)
            time = 0
            for p in piles:
                time += (p + mid - 1) // mid
            if time <= h:
                if lowestSpeed == 0:
                    lowestSpeed = mid
                else:
                    lowestSpeed = min(lowestSpeed, mid)
                high = mid - 1
            else:
                low = mid + 1
        return lowestSpeed


print(Solution().minEatingSpeed(piles=[1, 4, 3, 2], h=9))  # 2
print(Solution().minEatingSpeed(piles=[25, 10, 23, 4], h=4))  # 25
