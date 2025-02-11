class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = {}

        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                # insert (i+1,j), remove(i,j+1), replace(i+1,j+1)
                res = min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
                # adding 1 because at least one additional operation is needed
                dp[(i, j)] = res + 1

            return dp[(i, j)]

        return dfs(0, 0)


word1 = "monkeys"
word2 = "money"
print(Solution().minDistance(word1, word2))
