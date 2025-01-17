from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        def check(triplet):
            return all(t <= x for t, x in zip(triplet, target))

        res = [0, 0, 0]

        for triplet in triplets:
            if check(triplet):
                res = [max(r, t) for r, t in zip(res, triplet)]

        return res == target


triplets = [[1, 2, 3], [7, 1, 1]]
target = [7, 2, 3]
print(Solution().mergeTriplets(triplets, target))
triplets = [[2, 5, 6], [1, 4, 4], [5, 7, 5]]
target = [5, 4, 6]
print(Solution().mergeTriplets(triplets, target))
