from typing import List


class Solution:
    # works but slow
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.res = False

        def dfs(word, indx):
            if indx == len(s):
                if word == "":
                    self.res = True
                return
            for i in range(indx, len(s)):
                word += s[i]
                if word in wordDict:
                    dfs("", i+1)

        dfs("", 0)
        return self.res

    # dp
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]


s = "neetcode"
wordDict = ["neet", "code"]
print(Solution().wordBreak(s, wordDict))
s = "applepenapple"
wordDict = ["apple", "pen", "ape"]
print(Solution().wordBreak(s, wordDict))
s = "catsincars"
wordDict = ["cats", "cat", "sin", "in", "car"]
print(Solution().wordBreak(s, wordDict))
