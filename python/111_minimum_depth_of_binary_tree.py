# 111. Minimum Depth of Binary Tree - Easy

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Definition for a binary tree node.

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        level, stack = 0, deque([root])

        while stack:
            level += 1

            for x in range(len(stack)):
                n = stack.popleft()
                if not n.left and not n.right:
                    return level

                if n.left:
                    stack.append(n.left)
                if n.right:
                    stack.append(n.right)
