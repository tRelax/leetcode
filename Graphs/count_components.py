from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)

        components = 0

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return components


n = 3
edges = [[0, 1], [0, 2]]

print(Solution().countComponents(n, edges))  # 1 [0, 1, 2]

n = 6
edges = [[0, 1], [1, 2], [2, 3], [4, 5]]
print(Solution().countComponents(n, edges))  # 2 [0, 1, 2, 3] and [4, 5]
