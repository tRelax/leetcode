class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = {}, {}

        if len(s) != len(t):
            return False

        for c in list(s):
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1

        for c in list(t):
            if c in t_dict:
                t_dict[c] += 1
            else:
                t_dict[c] = 1

        return s_dict == t_dict
