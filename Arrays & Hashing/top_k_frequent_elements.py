from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = 1 + frequencies.get(num, 0)
        freq_sorted = dict(
            sorted(frequencies.items(), key=lambda item: item[1], reverse=True))
        return list(freq_sorted.keys())[:k]


sol = Solution()

print(sol.topKFrequent([1, 2, 3, 1, 2, 3, 3], 2))
