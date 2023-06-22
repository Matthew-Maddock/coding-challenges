# 714. Best Time to Buy and Sell Stock with Transaction Fee - Medium

# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:

from collections import defaultdict

# Input: prices = [1,3,2,8,4,9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# - Buying at prices[0] = 1
# - Selling at prices[3] = 8
# - Buying at prices[4] = 4
# - Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = defaultdict()

        def cost(i, n, bought_prev):
            if i >= n:
                return 0
            if (i, bought_prev) in dp:
                return dp[(i, bought_prev)]

            if bought_prev == True:
                dp[(i, bought_prev)] = max(cost(i + 1, n, False) + prices[i] - fee, cost(i + 1, n, bought_prev))
            else:
                dp[(i, bought_prev)] = max(cost(i + 1, n, True) - prices[i], cost(i + 1, n, bought_prev))
            return dp[(i, bought_prev)]

        return cost(0, len(prices), False)
