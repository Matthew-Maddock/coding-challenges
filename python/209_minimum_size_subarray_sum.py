# 209. Minimum Size Subarray Sum - Medium

# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
import math
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans = math.inf
        summ = 0
        j = 0

        for i, num in enumerate(nums):
            summ += num
            while summ >= s:
                ans = min(ans, i - j + 1)
                summ -= nums[j]
                j += 1

        return ans if ans != math.inf else 0
