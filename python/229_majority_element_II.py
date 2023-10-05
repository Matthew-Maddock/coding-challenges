# 229. Majority Element II - Medium

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) / 3
        cand = []

        hashMap = {num: 0 for num in nums}

        for num in nums:
            hashMap[num] += 1

        for key, count in zip(hashMap.keys(), hashMap.values()):
            if count > threshold:
                cand.append(key)

        return cand
