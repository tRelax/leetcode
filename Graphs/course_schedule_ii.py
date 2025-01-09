from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycle = set()
        visited = set()
        sol = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visited.add(crs)
            sol.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        for crs in range(numCourses):
            if crs not in sol:
                sol.append(crs)

        return sol


numCourses = 3
prerequisites = [[1, 0]]
print(Solution().findOrder(numCourses, prerequisites))  # [0, 1, 2]

numCourses = 3
prerequisites = [[0, 1], [1, 2], [2, 0]]
print(Solution().findOrder(numCourses, prerequisites))  # []
