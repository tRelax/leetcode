import string


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {letter: 0 for letter in string.ascii_lowercase}
        s2_map = {letter: 0 for letter in string.ascii_lowercase}
        for s in s1:
            s1_map[s] += 1

        l = 0
        for r in range(len(s2)):
            s2_map[s2[r]] += 1
            if s2_map == s1_map:
                return True
            elif sum(s2_map.values()) >= len(s1):
                s2_map[s2[l]] -= 1
                l += 1

        return False


s1 = "abc"
s2 = "lecabee"

print(s1, s2, Solution().checkInclusion(s1, s2))
