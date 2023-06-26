# 2462. Total Cost to Hire K Workers - Medium

# You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.

# You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:

# You will run k sessions and hire exactly one worker in each session.
# In each hiring session, choose the worker with the lowest cost from either the first candidates workers or the last candidates workers. Break the tie by the smallest index.
# For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session, we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
# In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
# If there are fewer than candidates workers remaining, choose the worker with the lowest cost among them. Break the tie by the smallest index.
# A worker can only be chosen once.
# Return the total cost to hire exactly k workers.

# Example 1:

# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Output: 11
# Explanation: We hire 3 workers in total. The total cost is initially 0.
# - In the first hiring round we choose the worker from [17,12,10,2,7,2,11,20,8]. The lowest cost is 2, and we break the tie by the smallest index, which is 3. The total cost = 0 + 2 = 2.
# - In the second hiring round we choose the worker from [17,12,10,7,2,11,20,8]. The lowest cost is 2 (index 4). The total cost = 2 + 2 = 4.
# - In the third hiring round we choose the worker from [17,12,10,7,11,20,8]. The lowest cost is 7 (index 3). The total cost = 4 + 7 = 11. Notice that the worker with index 3 was common in the first and last four workers.
# The total hiring cost is 11.
from typing import List
import heapq

class Solution:
  def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
    ans = 0
    i = 0
    j = len(costs) - 1
    minHeapL = []  # First half
    minHeapR = []  # Second half

    for _ in range(k):
      while len(minHeapL) < candidates and i <= j:
        heapq.heappush(minHeapL, costs[i])
        i += 1
      while len(minHeapR) < candidates and i <= j:
        heapq.heappush(minHeapR, costs[j])
        j -= 1
      if not minHeapL:
        ans += heapq.heappop(minHeapR)
      elif not minHeapR:
        ans += heapq.heappop(minHeapL)
      # Both `minHeapL` and `minHeapR` are not empty.
      elif minHeapL[0] <= minHeapR[0]:
        ans += heapq.heappop(minHeapL)
      else:
        ans += heapq.heappop(minHeapR)

    return ans

