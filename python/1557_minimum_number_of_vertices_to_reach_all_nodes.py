# 1557. Minimum Number of Vertices to Reach All Nodes - Medium

# Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

# Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

# Notice that you can return the vertices in any order.

# Example 1:

# Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
# Output: [0,3]
# Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, neighbors: List[List[int]]) -> List[int]:
        unreachables = set([i for i in range(n)])
        zero_indegree_nodes = set([i for i in range(n)])
        edges = {}
        for entry in neighbors:
            if entry[0] not in edges:
                edges[entry[0]] = []
            edges[entry[0]].append(entry[1])
            zero_indegree_nodes.discard(entry[1])
        # step 1: find all vertices with indegree = 0, traverse them and mark up reachable nodes
        result = list(zero_indegree_nodes)
        for node in zero_indegree_nodes:
            self._explore(node, unreachables, edges)
        # step 2: the rests are loops that are not connected -- also traverse and mark up
        while unreachables:
            result.append(min(unreachables))
            self._explore(min(unreachables), unreachables, edges)

        return sorted(result)

    def _explore(self, node, not_seen, edges):
        if node not in not_seen:
            return
        not_seen.remove(node)
        if node in edges:
            for neighbor in edges[node]:
                self._explore(neighbor, not_seen, edges)
