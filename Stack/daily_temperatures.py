from typing import List


class Solution:
    # Non stack solution
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        def helper(temp: int, temperatures: List[int]):
            if len(temperatures) == 0:
                return 0
            for i in range(len(temperatures)):
                if temp < temperatures[i]:
                    return i + 1
            return 0

        for i in range(len(temperatures)):
            res.append(helper(temperatures[i], temperatures[i+1:]))

        return res

    # Stack solution
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temperature, index]

        for indx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackIndx = stack.pop()
                res[stackIndx] = indx - stackIndx
            stack.append([temp, indx])
        return res


temperatures = [30, 38, 30, 36, 35, 40, 28]
# temperatures = [22, 21, 20]
print(Solution().dailyTemperatures(temperatures))
