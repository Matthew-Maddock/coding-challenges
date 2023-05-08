# 1572. Matrix Diagonal Sum - Easy

# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

# Example 1:


# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.


class Solution:
    def diagonalSum(self, mat):
        ans = 0
        for i in range(len(mat)):
            ans += mat[i][i] + mat[i][~i]
        if len(mat) % 2:
            ans -= mat[int(i / 2)][int(i / 2)]
        return ans
