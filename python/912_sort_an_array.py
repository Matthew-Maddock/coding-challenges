# 912. Sort an Array - Medium

# Given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        # quick sort

        self._merge_sort(nums, 0, len(nums) - 1)

        return nums

    def _merge_sort(self, nums, low, high):
        if low < high:

            mid = low + (high - low) // 2
            self._merge_sort(nums, low, mid)
            self._merge_sort(nums, mid + 1, high)
            self._merge(nums, low, high, mid)

    def _merge(self, nums, low, high, mid):
        i, j = low, mid + 1
        temp = []

        while i <= mid and j <= high:

            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1

            else:
                temp.append(nums[j])
                j += 1

        if i <= mid:
            temp.extend(nums[i : mid + 1])
        if j <= high:
            temp.extend(nums[j : high + 1])

        nums[low : high + 1] = temp
