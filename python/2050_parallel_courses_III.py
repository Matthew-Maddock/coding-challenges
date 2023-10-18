# 2050. Parallel Courses III - Hard

# You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given a 2D integer array relations where relations[j] = [prevCoursej, nextCoursej] denotes that course prevCoursej has to be completed before course nextCoursej (prerequisite relationship). Furthermore, you are given a 0-indexed integer array time where time[i] denotes how many months it takes to complete the (i+1)th course.

# You must find the minimum number of months needed to complete all the courses following these rules:

# You may start taking a course at any time if the prerequisites are met.
# Any number of courses can be taken at the same time.
# Return the minimum number of months needed to complete all the courses.

# Note: The test cases are generated such that it is possible to complete every course (i.e., the graph is a directed acyclic graph).

# Example 1:

import collections

# Input: n = 3, relations = [[1,3],[2,3]], time = [3,2,5]
# Output: 8
# Explanation: The figure above represents the given graph and the time required to complete each course.
# We start course 1 and course 2 simultaneously at month 0.
# Course 1 takes 3 months and course 2 takes 2 months to complete respectively.
# Thus, the earliest time we can start course 3 is at month 3, and the total time required is 3 + 5 = 8 months.
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        inDegree = [0] * n
        dist = time.copy()

        # Build graph.
        for a, b in relations:
            u = a - 1
            v = b - 1
            graph[u].append(v)
            inDegree[v] += 1

        # Topology
        q = collections.deque([i for i, d in enumerate(inDegree) if d == 0])

        while q:
            u = q.popleft()
            for v in graph[u]:
                dist[v] = max(dist[v], dist[u] + time[v])
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    q.append(v)

        return max(dist)
