# 989. Add to Array-Form of Integer - Easy

# The array-form of an integer num is an array representing its digits in left to right order.

# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.


# Example 1:

# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234

from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_A = int("".join(str(i) for i in num))
        res = list(str(num_A + k))
        res = list(map(int, res))
        return res
