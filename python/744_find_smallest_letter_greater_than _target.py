# 744. Find Smallest Letter Greater Than Target - Easy

# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

# Example 1:

# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
import bisect
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = bisect.bisect_right(range(len(letters)), target, key=lambda m: letters[m])
        return letters[l % len(letters)]
