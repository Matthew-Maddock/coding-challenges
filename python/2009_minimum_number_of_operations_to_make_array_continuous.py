# 2009. Minimum Number of Operations to Make Array Continuous - Hard

# You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

# nums is considered continuous if both of the following conditions are fulfilled:

# All elements in nums are unique.
# The difference between the maximum element and the minimum element in nums equals nums.length - 1.
# For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

# Return the minimum number of operations to make nums continuous.

# Example 1:

# Input: nums = [4,2,5,3]
# Output: 0
# Explanation: nums is already continuous.
# Example 2:

from bisect import bisect_right

# Input: nums = [1,2,3,5,6]
# Output: 1
# Explanation: One possible solution is to change the last element to 4.
# The resulting array is [1,2,3,5,4], which is continuous.
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        nums = sorted(set(nums))

        for i, start in enumerate(nums):
            end = start + n - 1
            index = bisect_right(nums, end)
            uniqueLength = index - i
            ans = min(ans, n - uniqueLength)

        return ans
