# 1027. Longest Arithmetic Subsequence - Medium

# Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

# Note that:

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
# A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).


# Example 1:

# Input: nums = [3,6,9,12]
# Output: 4
# Explanation:  The whole array is an arithmetic sequence with steps of length = 3.
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        dp = [[0] * 1001 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                k = nums[i] - nums[j] + 500
                dp[i][k] = max(2, dp[j][k] + 1)
                ans = max(ans, dp[i][k])

        return ans
