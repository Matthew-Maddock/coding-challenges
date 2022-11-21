# 9. Palindrome Number - Easy

# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        List = [i for i in str(x)]
        
        if List == List[::-1]:
            return True
        else: 
            return False
        