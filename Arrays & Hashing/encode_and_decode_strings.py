from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        returned_string = ""
        for s in strs:
            returned_string += s + "?XD?"
        return returned_string

    def decode(self, s: str) -> List[str]:
        original_strs = s.split("?XD?")
        original_strs.pop()
        return original_strs


sol = Solution()

enc = sol.encode(["wow", "veri_nice"])
print(enc)

dec = sol.decode(enc)
print(dec)
