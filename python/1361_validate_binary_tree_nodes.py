# 1361. Validate Binary Tree Nodes - Medium

# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

# Note that the nodes have no values and that we only use the node numbers in this problem.

# Example 1:

# Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# Output: true
from collections import defaultdict


class Solution:
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        graph = defaultdict(list)
        in_degree = [0] * n

        for node in range(n):
            left, right = leftChild[node], rightChild[node]
            if left != -1:
                graph[node].append(left)
                in_degree[left] += 1
            if right != -1:
                graph[node].append(right)
                in_degree[right] += 1

        root_candidates = [node for node in range(n) if in_degree[node] == 0]

        if len(root_candidates) != 1:
            return False
        root = root_candidates[0]

        queue = [root]
        seen = set([root])

        while queue:
            node = queue.pop(0)
            if node in graph:
                for child in graph[node]:
                    if child in seen:
                        return False
                    seen.add(child)
                    queue.append(child)

        return len(seen) == n
