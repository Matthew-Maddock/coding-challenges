# 863. All Nodes Distance K in Binary Tree - Medium

# Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

# You can return the answer in any order.

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.

from collections import defaultdict, deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def connect_parent(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                connect_parent(cur.left, cur)
            if cur.right:
                connect_parent(cur.right, cur)

        connect_parent(root, None)

        answer = []
        visited = set([target.val])
        queue = deque([(target.val, 0)])

        while queue:
            curr, distance = queue.popleft()
            if distance == k:
                answer.append(curr)
                continue
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
                    visited.add(neighbor)
