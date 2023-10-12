# 1095. Find in Mountain Array - Hard

# (This problem is an interactive problem.)

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

# You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

# MountainArray.get(k) returns the element of the array at index k (0-indexed).
# MountainArray.length() returns the length of the array.
# Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.


# Example 1:

# Input: array = [1,2,3,4,5,3,1], target = 3
# Output: 2
# Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
# Example 2:

# Input: array = [0,1,2,4,2,1], target = 3
# Output: -1
# Explanation: 3 does not exist in the array, so we return -1.


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def get(self, index: int) -> int:
        ...

    def length(self) -> int:
        ...


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        n = mountain_arr.length()
        peakIndex = self.peakIndexInMountainArray(mountain_arr, 0, n - 1)

        leftIndex = self.searchLeft(mountain_arr, target, 0, peakIndex)
        if mountain_arr.get(leftIndex) == target:
            return leftIndex

        rightIndex = self.searchRight(mountain_arr, target, peakIndex + 1, n - 1)
        if mountain_arr.get(rightIndex) == target:
            return rightIndex

        return -1

    # 852. Peak Index in a Mountain Array
    def peakIndexInMountainArray(self, A: "MountainArray", l: int, r: int) -> int:
        while l < r:
            m = (l + r) // 2
            if A.get(m) < A.get(m + 1):
                l = m + 1
            else:
                r = m
        return l

    def searchLeft(self, A: "MountainArray", target: int, l: int, r: int) -> int:
        while l < r:
            m = (l + r) // 2
            if A.get(m) < target:
                l = m + 1
            else:
                r = m
        return l

    def searchRight(self, A: "MountainArray", target: int, l: int, r: int) -> int:
        while l < r:
            m = (l + r) // 2
            if A.get(m) > target:
                l = m + 1
            else:
                r = m
        return l
