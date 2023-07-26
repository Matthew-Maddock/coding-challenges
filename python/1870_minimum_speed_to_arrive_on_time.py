# 1870. Minimum Speed to Arrive on Time - Medium

# You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

# Each train can only depart at an integer hour, so you may need to wait in between each train ride.

# For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
# Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

# Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.

# Example 1:

import math

# Input: dist = [1,3,2], hour = 6
# Output: 1
# Explanation: At speed 1:
# - The first train ride takes 1/1 = 1 hour.
# - Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
# - Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
# - You will arrive at exactly the 6 hour mark.
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        ans = -1
        l = 1
        r = int(1e7)

        def time(speed: int) -> float:
            summ = 0
            for i in range(len(dist) - 1):
                summ += math.ceil(dist[i] / speed)
            return summ + dist[-1] / speed

        while l <= r:
            m = (l + r) // 2
            if time(m) > hour:
                l = m + 1
            else:
                ans = m
                r = m - 1

        return ans
