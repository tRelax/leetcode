from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        sol = []

        def backtrack(op: int, close: int) -> str:
            if op == close == n:
                sol.append("".join(stack))
                return
            if op < n:
                stack.append("(")
                backtrack(op + 1, close)
                stack.pop()
            if close < op:
                stack.append(")")
                backtrack(op, close + 1)
                stack.pop()

        backtrack(0, 0)

        return sol


num = 1
# # ["()"]
num = 2
# # ["(())", "()()"]
num = 3
# # ["((()))","(()())","(())()","()(())","()()()"]
print(Solution().generateParenthesis(num))
