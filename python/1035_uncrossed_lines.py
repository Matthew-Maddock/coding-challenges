# 1035. Uncrossed Lines - Medium

# You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

# nums1[i] == nums2[j], and
# the line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

# Return the maximum number of connecting lines we can draw in this way.

# Example 1:

# Input: nums1 = [1,4,2], nums2 = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for j in range(len(B))] for i in range(len(A))]
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if a == b:
                    if i >= 1 and j >= 1:
                        dp[i][j] = max(dp[i][j], 1 + dp[i - 1][j - 1])
                    else:
                        dp[i][j] = max(dp[i][j], 1)
        return dp[len(A) - 1][len(B) - 1]
