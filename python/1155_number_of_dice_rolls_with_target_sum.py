# 1155. Number of Dice Rolls With Target Sum - Medium

# You have n dice, and each die has k faces numbered from 1 to k.

# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

# Example 1:

# Input: n = 1, k = 6, target = 3
# Output: 1
# Explanation: You throw one die with 6 faces.
# There is only one way to get a sum of 3.
# Example 2:


# Input: n = 2, k = 6, target = 7
# Output: 6
# Explanation: You throw two dice, each with 6 faces.
# There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        kMod = 1_000_000_007
        dp = [1] + [0] * target

        for _ in range(n):  # n dices
            newDp = [0] * (target + 1)
            for i in range(1, k + 1):  # numbers 1, 2, ..., f
                for t in range(i, target + 1):  # all the possible targets
                    newDp[t] += dp[t - i]
                    newDp[t] %= kMod
            dp = newDp

        return dp[target]
