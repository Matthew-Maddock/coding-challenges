# 87. Scramble String - Hard

# We can scramble a string s to get a string t using the following algorithm:

# If the length of the string is 1, stop.
# If the length of the string is > 1, do the following:
# Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
# Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
# Apply step 1 recursively on each of the two substrings x and y.
# Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.


# Example 1:

# Input: s1 = "great", s2 = "rgeat"
# Output: true
# Explanation: One possible scenario applied on s1 is:
# "great" --> "gr/eat" // divide at random index.
# "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings and keep them in order.
# "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both substrings. divide at random index each of them.
# "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first substring and to keep the second substring in the same order.
# "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively, divide "at" to "a/t".
# "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both substrings in the same order.
# The algorithm stops now, and the result string is "rgeat" which is s2.
# As one possible scenario led s1 to be scrambled to s2, we return true.


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # DP -- scramble[i][j][k]: s1[i:i+k] and s2[j:j+k] is scramble (substring of length k, starting at position i and j for s1 and s2)
        # scramble[i][j][k] = (scramble[i][j][l] and scramble[i+l][j+l][k-l]) or (scramble[i][j+k-l][l] and scramble[i+l][j][k-l])
        scramble = [[[False] * (len(s1) + 1) for _ in range(len(s1))] for _ in range(len(s1))]
        for k in range(1, len(s1) + 1):
            for i in range(len(s1) - k + 1):
                for j in range(len(s1) - k + 1):
                    if k == 1:
                        scramble[i][j][k] = s1[i] == s2[j]
                    else:
                        is_scramble = False
                        for l in range(1, k):
                            if (scramble[i][j][l] and scramble[i + l][j + l][k - l]) or (
                                scramble[i][j + k - l][l] and scramble[i + l][j][k - l]
                            ):
                                is_scramble = True
                                break
                        scramble[i][j][k] = is_scramble

        return scramble[0][0][len(s1)]
