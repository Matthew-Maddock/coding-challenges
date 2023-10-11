# 2251. Number of Flowers in Full Bloom - Hard

# You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array people of size n, where people[i] is the time that the ith person will arrive to see the flowers.

# Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

# Example 1:

import bisect

# Input: flowers = [[1,6],[3,7],[9,12],[4,13]], poeple = [2,3,7,11]
# Output: [1,2,2,2]
# Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
# For each person, we return the number of flowers in full bloom during their arrival.
from typing import List


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        starts = sorted(s for s, _ in flowers)
        ends = sorted(e for _, e in flowers)
        return [bisect.bisect_right(starts, person) - bisect.bisect_left(ends, person) for person in persons]
