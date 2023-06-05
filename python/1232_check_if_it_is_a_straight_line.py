# 1232. Check If It Is a Straight Line - Easy

# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# Example 1:

# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # for starters lets find the equation of the line created by the first two points
        if (coordinates[1])[0] == (coordinates[0])[0]:
            for i in range(2, len(coordinates)):
                if (coordinates[i - 1])[0] != (coordinates[i])[0]:
                    return False
            return True
        else:
            l = ((coordinates[1])[1] - (coordinates[0])[1]) / ((coordinates[1])[0] - (coordinates[0])[0])
        b = (coordinates[0])[1] - l * (coordinates[0])[0]

        # iterate over list and see if the rest of the points belong to the same line
        for i in range(2, len(coordinates)):
            if (coordinates[i])[1] != l * (coordinates[i])[0] + b:
                return False
        return True
