# 1287. Element Appearing More Than 25% In Sorted Array - Easy

# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

# Example 1:

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# Example 2:

# Input: arr = [1,1]
# Output: 1
from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cutoff = len(arr) * 0.25
        counts = Counter(arr)

        for key, val in zip(counts.keys(), counts.values()):
            if val > cutoff:
                return key

        return None
