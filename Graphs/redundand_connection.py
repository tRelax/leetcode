from typing import List


class Solution:
    # union find
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        ranks = [1] * (len(edges) + 1)

        def find(node):
            p = parents[node]
            while p != parents[p]:
                # setting up for future lookups
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def union(u, v):
            pu, pv = find(u), find(v)
            # if they are already in the same set, then adding this edge will create a cycle
            if pu == pv:
                return False
            if ranks[pu] > ranks[pv]:
                parents[pv] = pu
                ranks[pu] += ranks[pv]
            else:
                parents[pu] = pv
                ranks[pv] += ranks[pu]
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]


edges = [[1, 2], [1, 3], [3, 4], [2, 4]]
print(Solution().findRedundantConnection(edges))  # [2, 4]
edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
print(Solution().findRedundantConnection(edges))  # [3, 4]
