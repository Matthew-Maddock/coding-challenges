# 1647. Minimum Deletions to Make Character Frequencies Unique - Medium

# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

# Example 1:

# Input: s = "aab"
# Output: 0
# Explanation: s is already good.
import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        ans = 0
        count = collections.Counter(s)
        usedFreq = set()

        for freq in count.values():
            while freq > 0 and freq in usedFreq:
                freq -= 1  # Delete ('a' + i).
                ans += 1
            usedFreq.add(freq)

        return ans
