# 15. 3Sum - Medium
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.


# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the given array
        nums.sort()
        # Length of the array
        n = len(nums)
        # Resultant list
        triplets = list()
        # Loop for each character in the array
        for i in range(0, n):
            # Avoid duplicates due to i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Left and right pointers
            j = i + 1
            k = n - 1
            # Loop for remaining pairs
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # Avoid duplicates for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return triplets
