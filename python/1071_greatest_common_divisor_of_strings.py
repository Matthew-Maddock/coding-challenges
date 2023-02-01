# 1071. Greatest Common Divisor of Strings - Easy

# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def mod(s1: str, s2: str) -> str:
            while s1.startswith(s2):
                s1 = s1[len(s2) :]
            return s1

        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        if not str1.startswith(str2):
            return ""
        if not str2:
            return str1
        return self.gcdOfStrings(str2, mod(str1, str2))
