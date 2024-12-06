from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, h = 0, ROWS * COLS - 1
        while l <= h:
            m = l + ((h-l) // 2)
            mR = m // COLS
            mC = m % COLS
            if matrix[mR][mC] < target:
                l = m + 1
            elif matrix[mR][mC] > target:
                h = m - 1
            else:
                return True
        return False


print(Solution().searchMatrix(matrix=[[1, 2, 4, 8], [
      10, 11, 12, 13], [14, 20, 30, 40]], target=10))

print(Solution().searchMatrix(matrix=[[1, 2, 4, 8], [
      10, 11, 12, 13], [14, 20, 30, 40]], target=15))
