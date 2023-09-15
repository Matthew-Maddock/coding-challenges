# 1584. Min Cost to Connect All Points - Medium

# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

# Example 1:


# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation:

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
import math
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[int]) -> int:
        # dist[i] := min distance to connect points[i]
        dist = [math.inf] * len(points)
        ans = 0

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                # Try to connect points[i] with points[j].
                dist[j] = min(dist[j], abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))
                # Swap points[j] (point with min dist) with points[i + 1].
                if dist[j] < dist[i + 1]:
                    points[j], points[i + 1] = points[i + 1], points[j]
                    dist[j], dist[i + 1] = dist[i + 1], dist[j]
            ans += dist[i + 1]

        return ans
