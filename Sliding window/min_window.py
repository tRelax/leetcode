import string


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        res = ""
        l = 0
        s_map = {letter: 0 for letter in string.ascii_letters}

        for c in t:
            if c in t_map:
                t_map[c] += 1
            else:
                t_map[c] = 1

        for r in range(len(s)):

            s_map[s[r]] += 1
            while all(s_map.get(key, float('-inf')) >= value for key, value in t_map.items()):
                res = s[l:r+1]
                s_map[s[l]] -= 1
                l+=1
            

        return res


s = "OUZODYXAZV"
t = "XYZ"
print(Solution().minWindow(s, t))

s = "xyz"
t = "xyz"
print(Solution().minWindow(s, t))

s = "x"
t = "xy"
print(Solution().minWindow(s, t))

s="ADOBECODEBANC"
t="ABC"
print(Solution().minWindow(s, t))



