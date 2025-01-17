from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []

        last = {c: i for i, c in enumerate(s)}
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])

            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res


s = "xyxxyzbzbbisl"
print(Solution().partitionLabels(s))
# "xyxxyzbzbbisl" -> {x:3, y:4, z:7, b:9, i:10, s:11, l:12} -> 5, 5, 1, 1, 1
