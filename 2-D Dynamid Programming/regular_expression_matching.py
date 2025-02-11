class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = {}

        def dfs(i, j):
            if j == n:
                return i == m
            if (i, j) in dp:
                return dp[(i, j)]

            isMatching = i < m and (s[i] == p[j] or p[j] == ".")

            if (j+1) < n and p[j+1] == "*":
                dp[(i, j)] = (dfs(i, j+2) or isMatching and dfs(i+1, j))
                return dp[(i, j)]
            if isMatching:
                dp[(i, j)] = dfs(i+1, j+1)
                return dp[(i, j)]

            dp[(i, j)] = False
            return False

        return dfs(0, 0)


s = "aa"
p = ".b"
print(Solution().isMatch(s, p))
