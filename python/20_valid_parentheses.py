# 20. Valid Parentheses - Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        # Stack for left symbols
        stack = []
        # Loop for each character of the string
        for c in s:
            # If left symbol is encountered
            if c in ["(", "{", "["]:
                stack.append(c)
            # If right symbol is encountered
            elif c == ")" and len(stack) != 0 and stack[-1] == "(":

                stack.pop()
            elif c == "}" and len(stack) != 0 and stack[-1] == "{":
                stack.pop()
            elif c == "]" and len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            # If none of the valid symbols is encountered
            else:
                return False
        return stack == []
