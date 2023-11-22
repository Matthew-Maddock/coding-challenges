# 1424. Diagonal Traverse II - Medium

# Companies
# Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

# Example 1:

# Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,4,2,7,5,3,8,6,9]
# Example 2:

# Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, A: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(A)):
            for j in range(len(A[i])):
                d[i + j].append(A[i][j])
        return [v for k in d.keys() for v in reversed(d[k])]
