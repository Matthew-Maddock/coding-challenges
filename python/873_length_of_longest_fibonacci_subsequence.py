# 873. Length of Longest Fibonacci Subsequence - Medium

# A sequence x1, x2, ..., xn is Fibonacci-like if:

# n >= 3
# xi + xi+1 == xi+2 for all i + 2 <= n
# Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

# A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].


# Example 1:

# Input: arr = [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].

import collections
from typing import List


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        vals_from_idx_i = collections.defaultdict(set)
        vals_from_idx_i[len(A) - 1] = {A[-1]}
        for i in range(len(A) - 1, -1, -1):
            vals_from_idx_i[i] = vals_from_idx_i[i + 1] | {A[i]}

        def dfs():
            fin_res = 2
            open_list = []
            for i in range(len(A) - 2):
                for j in range(i + 1, len(A) - 1):
                    new_a = A[i] + A[j]
                    if new_a in vals_from_idx_i[j + 1]:
                        fin_res = 3
                        idx = A[j + 1 :].index(new_a)
                        open_list.append((A[j], new_a, j + idx + 1, 3))
            while open_list:
                a, b, j, d = open_list.pop()
                new_a = a + b
                if new_a in vals_from_idx_i[j + 1]:
                    if d + 1 > fin_res:
                        fin_res = d + 1
                    idx = A[j + 1 :].index(new_a)
                    new_idx = j + idx + 1
                    # early pruning
                    if d + 1 + (len(A) - 1 - new_idx) > fin_res:
                        open_list.append((b, new_a, new_idx, d + 1))
            return fin_res

        fin_res = dfs()
        return fin_res if fin_res > 2 else 0
