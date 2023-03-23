# 1319. Number of Operations to Make Network Connected - Medium

# There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

# You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

# Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = {i: i for i in range(n)}

        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(a, b):
            uf[find(a)] = find(b)

        if len(connections) < n - 1:
            return -1
        for a, b in connections:
            union(a, b)
        islands = len({find(x) for x in uf})
        return islands - 1
