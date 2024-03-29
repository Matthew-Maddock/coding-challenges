# 823. Binary Trees With Factors - Medium

# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

# We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

# Example 1:

# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]

from typing import List


class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        dp = {}
        for a in sorted(A):
            dp[a] = sum(dp[b] * dp.get(a // b, 0) for b in dp if a % b == 0) + 1
        return sum(dp.values()) % (10**9 + 7)
