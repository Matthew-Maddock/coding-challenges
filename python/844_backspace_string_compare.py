# 844. Backspace String Compare - Easy

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stripped = ""
        t_stripped = ""

        for char in s:
            if char == "#":
                s_stripped = s_stripped[:-1]
            else:
                s_stripped += char

        for char in t:
            if char == "#":
                t_stripped = t_stripped[:-1]
            else:
                t_stripped += char

        return s_stripped == t_stripped
