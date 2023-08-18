# 1615. Maximal Network Rank - Medium

# There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

# The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

# Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

# Example 1:

# Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
# Output: 4
# Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.
import collections


class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        MAX_N = 100
        MAX_NUM = MAX_N - 1

        def counting_sort(arr, key=lambda x: x, reverse=False):  # Time: O(n), Space: O(n)
            count = [0] * (MAX_NUM + 1)
            for x in arr:
                count[key(x)] += 1
            for i in range(1, len(count)):
                count[i] += count[i - 1]
            result = [0] * len(arr)
            if not reverse:
                for x in reversed(arr):  # stable sort
                    count[key(x)] -= 1
                    result[count[key(x)]] = x
            else:
                for x in arr:  # stable sort
                    count[key(x)] -= 1
                    result[count[key(x)]] = x
                result.reverse()
            return result

        degree = [0] * n
        adj = collections.defaultdict(set)
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            adj[a].add(b)
            adj[b].add(a)
        sorted_idx = counting_sort(range(n), key=lambda x: degree[x], reverse=True)
        m = 2
        while m < n:
            if degree[sorted_idx[m]] != degree[sorted_idx[1]]:
                break
            m += 1
        result = degree[sorted_idx[0]] + degree[sorted_idx[1]] - 1  # at least sum(top2 values) - 1
        for i in range(m - 1):  # only need to check pairs of top2 values
            for j in range(i + 1, m):
                if (
                    degree[sorted_idx[i]]
                    + degree[sorted_idx[j]]
                    - int(sorted_idx[i] in adj and sorted_idx[j] in adj[sorted_idx[i]])
                    > result
                ):  # if equal to ideal sum of top2 values, break
                    return (
                        degree[sorted_idx[i]]
                        + degree[sorted_idx[j]]
                        - int(sorted_idx[i] in adj and sorted_idx[j] in adj[sorted_idx[i]])
                    )
        return result
