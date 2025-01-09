from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereqMap[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if prereqMap[crs] == []:
                return True

            visited.add(crs)
            for pre in prereqMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            prereqMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True


numCourses = 2
prerequisites = [[0, 1]]
print(Solution().canFinish(numCourses, prerequisites))  # True
numCourses = 2
prerequisites = [[0, 1], [1, 0]]
print(Solution().canFinish(numCourses, prerequisites))  # False
