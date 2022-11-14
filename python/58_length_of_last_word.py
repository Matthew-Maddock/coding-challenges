# 58. Length of Last Word - Easy

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        StringList = s.split(" ")
        res = ''
        
        for char in StringList[::-1]:
            
            if char != '':
                res = len(char)
                break
                
        return res
                
        