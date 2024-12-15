from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def backtrack(i, cur_str):
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i+1, cur_str + c)

        if digits:
            backtrack(0, "")
        return res


Solution().letterCombinations("23")
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
