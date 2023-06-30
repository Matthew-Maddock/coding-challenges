# 1970. Last Day Where You Can Still Cross - Hard

# There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

# Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

# You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

# Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

# Example 1:

# Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
# Output: 2
# Explanation: The above image depicts how the matrix changes each day starting from day 0.
# The last day where it is possible to cross from top to bottom is on day 2.
import collections
from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dirs = [0, 1, 0, -1, 0]

        def canWalk(day: int) -> bool:
            matrix = [[0] * col for _ in range(row)]
            for i in range(day):
                x, y = cells[i]
                matrix[x - 1][y - 1] = 1

            q = collections.deque()

            for j in range(col):
                if matrix[0][j] == 0:
                    q.append((0, j))
                    matrix[0][j] = 1

            while q:
                i, j = q.popleft()
                for k in range(4):
                    x = i + dirs[k]
                    y = j + dirs[k + 1]
                    if x < 0 or x == row or y < 0 or y == col:
                        continue
                    if matrix[x][y] == 1:
                        continue
                    if x == row - 1:
                        return True
                    q.append((x, y))
                    matrix[x][y] = 1

            return False

        ans = 0
        l = 1
        r = len(cells) - 1

        while l <= r:
            m = (l + r) // 2
            if canWalk(m):
                ans = m
                l = m + 1
            else:
                r = m - 1

        return ans
