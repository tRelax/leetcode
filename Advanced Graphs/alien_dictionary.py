from typing import List


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # comparing all characters, and if a char is different, add char from w2[j] to w1[j]
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # False = visited, True = in current path
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True

            for nei in adj[c]:
                # if char is already in current path then return true, there must be a cycle -> invalid
                if dfs(nei):
                    return True

            visited[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)


words = ["hrn", "hrf", "er", "enn", "rfnn"]
print(Solution().foreignDictionary(words))
