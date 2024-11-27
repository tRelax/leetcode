from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [[pos, speed]
                  for pos, speed in zip(position, speed)]  # [pos, speed]
        stack = []
        for pos, speed in sorted(fleets)[::-1]:
            stack.append((target-pos)/speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


target = 10
position = [1, 4]
speed = [3, 2]
# 1

# print(Solution().carFleet(target, position, speed))

target = 10
position = [4, 1, 0, 7]
speed = [2, 2, 1, 1]
# 3
print(Solution().carFleet(target, position, speed))

target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
print(Solution().carFleet(target, position, speed))
