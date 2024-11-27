from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token))

        return stack.pop()


tokens = ["1", "2", "+", "3", "*", "4", "-"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(tokens))
