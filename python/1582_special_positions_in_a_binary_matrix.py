# 1582. Special Positions in a Binary Matrix - Easy

# Given an m x n binary matrix mat, return the number of special positions in mat.

# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

# Example 1:

# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

# Example 2:

# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
# Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        ans = 0
        rowOnes = [0] * m
        colOnes = [0] * n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    rowOnes[i] += 1
                    colOnes[j] += 1

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rowOnes[i] == 1 and colOnes[j] == 1:
                    ans += 1

        return ans
