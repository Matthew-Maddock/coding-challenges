# 1768. Merge Strings Alternately - Easy

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

from itertools import zip_longest


class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
