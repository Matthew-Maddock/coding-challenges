# 673. Number of Longest Increasing Subsequence - Medium

# Given an integer array nums, return the number of longest increasing subsequences.

# Notice that the sequence has to be strictly increasing.

# Example 1:

# Input: nums = [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        ans = 0
        maxLength = 0
        length = [1] * len(nums)  # length[i] := LIS's length ending w/ nums[i]
        count = [1] * len(nums)  # count[i] := # of the LIS ending w/ nums[i]

        # Calculate length and count arrays
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < num:
                    if length[i] < length[j] + 1:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[i] == length[j] + 1:
                        count[i] += count[j]

        # Get # Of LIS
        for i, l in enumerate(length):
            if l > maxLength:
                maxLength = l
                ans = count[i]
            elif l == maxLength:
                ans += count[i]

        return ans
