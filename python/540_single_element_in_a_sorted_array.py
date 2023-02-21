# 540. Single Element in a Sorted Array - Medium

# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.


# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            m = l + ((r - l) // 2)
            if (m - 1 < 0 or nums[m - 1] != nums[m]) and (m + 1 == len(nums) or nums[m + 1] != nums[m]):

                return nums[m]

            leftSide = m - 1 if nums[m - 1] == nums[m] else m

            if leftSide % 2:

                r = m - 1

            else:

                l = m + 1
