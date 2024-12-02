class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        alp_set = set(s)
        mp = {element: 0 for element in alp_set}
        for r in range(len(s)):
            mp[s[r]] += 1
            max_item = max(mp.values())
            if sum(mp.values()) - max_item > k:
                mp[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)

        return res


s = "XYYX"
k = 2
print(s, Solution().characterReplacement(s, k))

s = "AAABABB"
k = 1
print(s, Solution().characterReplacement(s, k))

s = "XYZXY"
k = 2
print(s, Solution().characterReplacement(s, k))

s = "ABAA"
k = 0
print(s, Solution().characterReplacement(s, k))

s = "AABABBA"
k = 1
print(s, Solution().characterReplacement(s, k))
