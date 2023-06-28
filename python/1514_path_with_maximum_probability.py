# 1514. Path with Maximum Probability - Medium

# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

# Example 1:

# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
# Output: 0.25000
# Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
import heapq
from typing import List

class Solution:
  def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    graph = [[] for _ in range(n)]  # [a: [(b, prob_ab)]]
    maxHeap = [(-1.0, start)]   # (prob to reach u, u)
    seen = [False] * n

    for i, ((u, v), prob) in enumerate(zip(edges, succProb)):
      graph[u].append((v, prob))
      graph[v].append((u, prob))

    while maxHeap:
      prob, u = heapq.heappop(maxHeap)
      prob *= -1
      if u == end:
        return prob
      if seen[u]:
        continue
      seen[u] = True
      for nextNode, edgeProb in graph[u]:
        if seen[nextNode]:
          continue
        heapq.heappush(maxHeap, (-prob * edgeProb, nextNode))

    return 0