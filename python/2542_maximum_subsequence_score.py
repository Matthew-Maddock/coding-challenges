# 2542. Maximum Subsequence Score - Medium

# You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k. You must choose a subsequence of indices from nums1 of length k.

# For chosen indices i0, i1, ..., ik - 1, your score is defined as:

# The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
# It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
# Return the maximum possible score.

# A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.

# Example 1:


# Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
# Output: 12
# Explanation:
# The four possible subsequence scores are:
# - We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
# - We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6.
# - We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12.
# - We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
# Therefore, we return the max score, which is 12.

import heapq
from typing import List


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        minHeap = []

        n1Sum = 0
        res = 0

        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(minHeap, n1)

            if len(minHeap) > k:
                n1Pop = heapq.heappop(minHeap)
                n1Sum -= n1Pop

            if len(minHeap) == k:
                res = max(res, n1Sum * n2)

        return res
