# 2448. Minimum Cost to Make Array Equal - Hard

# You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

# You can do the following operation any number of times:

# Increase or decrease any element of the array nums by 1.
# The cost of doing one operation on the ith element is cost[i].

# Return the minimum total cost such that all the elements of the array nums become equal.

# Example 1:

# Input: nums = [1,3,5,2], cost = [2,3,1,14]
# Output: 8
# Explanation: We can make all the elements equal to 2 in the following way:
# - Increase the 0th element one time. The cost is 2.
# - Decrease the 1st element one time. The cost is 3.
# - Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
# The total cost is 2 + 3 + 3 = 8.
# It can be shown that we cannot make the array equal with a smaller cost.
from typing import List


class Solution:
    def calculateSum(self, nums, cost, target):
        res = 0
        for n, c in zip(nums, cost):
            res += abs(n - target) * c
        return res

    def minCost(self, nums: List[int], cost: List[int]) -> int:
        s, e = min(nums), max(nums)

        while s < e:
            mid = (s + e) // 2
            leftSum, rightSum = self.calculateSum(nums, cost, mid), self.calculateSum(nums, cost, mid + 1)
            if leftSum < rightSum:
                e = mid
            else:
                s = mid + 1

        return self.calculateSum(nums, cost, s)
