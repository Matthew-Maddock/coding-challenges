# 459. Repeated Substring Pattern - Easy

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
