# 239. Sliding Window Maximum - Hard

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

# Example 1:

import collections

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = collections.deque()  # Max queue

        for i, num in enumerate(nums):
            while dq and dq[-1] < num:
                dq.pop()
            dq.append(num)
            if i >= k and nums[i - k] == dq[0]:  # Out of bound
                dq.popleft()
            if i >= k - 1:
                ans.append(dq[0])

        return ans
