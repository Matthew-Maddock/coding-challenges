# 1743. Restore the Array From Adjacent Pairs - Medium

# There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

# You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

# It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

# Return the original array nums. If there are multiple solutions, return any of them.

# Example 1:

# Input: adjacentPairs = [[2,1],[3,4],[3,2]]
# Output: [1,2,3,4]
# Explanation: This array has all its adjacent pairs in adjacentPairs.
# Notice that adjacentPairs[i] may not be in left-to-right order.
# Example 2:

# Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
# Output: [-2,4,1,-3]
# Explanation: There can be negative numbers.
# Another solution is [-3,1,4,-2], which would also be accepted.
# Example 3:

# Input: adjacentPairs = [[100000,-100000]]
# Output: [100000,-100000]
import collections
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        ans = []
        numToAdjs = collections.defaultdict(list)

        for a, b in adjacentPairs:
            numToAdjs[a].append(b)
            numToAdjs[b].append(a)

        for num, adjs in numToAdjs.items():
            if len(adjs) == 1:
                ans.append(num)
                ans.append(adjs[0])
                break

        while len(ans) < len(adjacentPairs) + 1:
            tail = ans[-1]
            prev = ans[-2]
            adjs = numToAdjs[tail]
            if adjs[0] == prev:  # adjs[0] is already used
                ans.append(adjs[1])
            else:
                ans.append(adjs[0])

        return ans
