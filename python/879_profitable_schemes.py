# 879. Profitable Schemes - Hard

# There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

# Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.

# Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.

# Example 1:

# Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# Output: 2
# Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
# In total, there are 2 schemes.

from typing import List


class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        # dp[g][p]
        dp = [[0] * (G + 1) for i in range(P + 1)]
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for i in range(P, -1, -1):
                for j in range(G - g, -1, -1):
                    dp[min(P, i + p)][j + g] += dp[i][j]
        return sum(dp[P]) % (10**9 + 7)
