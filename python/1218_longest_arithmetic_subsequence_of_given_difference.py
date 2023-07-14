# 1218. Longest Arithmetic Subsequence of Given Difference - Medium

# Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

# A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

# Example 1:

# Input: arr = [1,2,3,4], difference = 1
# Output: 4
# Explanation: The longest arithmetic subsequence is [1,2,3,4].
from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 0
        lengthAt = {}

        for a in arr:
            lengthAt[a] = lengthAt.get(a - difference, 0) + 1
            ans = max(ans, lengthAt[a])

        return ans
