from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        candidates.sort()

        def backtrack(i, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return

            # include the number
            cur.append(candidates[i])
            backtrack(i+1, sum(cur))
            cur.pop()
            # dont include the number or its duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, sum(cur))

        backtrack(0, 0)
        return res


Solution().combinationSum2(candidates=[9, 2, 2, 4, 6, 1, 5], target=8)
Solution().combinationSum2(candidates=[1, 2, 3, 4, 5], target=7)
