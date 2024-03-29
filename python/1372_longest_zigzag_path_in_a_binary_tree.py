# 1372. Longest ZigZag Path in a Binary Tree - Medium

# You are given the root of a binary tree.

# A ZigZag path for a binary tree is defined as follow:

# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

# Return the longest ZigZag path contained in that tree.

# Example 1:

# Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
# Output: 3
# Explanation: Longest ZigZag path in blue nodes (right -> left -> right).

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class T:
    def __init__(self, leftMax: int, rightMax: int, subtreeMax: int):
        self.leftMax = leftMax
        self.rightMax = rightMax
        self.subtreeMax = subtreeMax


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> T:
            if not root:
                return T(-1, -1, -1)
            left = dfs(root.left)
            right = dfs(root.right)
            leftZigZag = left.rightMax + 1
            rightZigZag = right.leftMax + 1
            subtreeMax = max(leftZigZag, rightZigZag, left.subtreeMax, right.subtreeMax)
            return T(leftZigZag, rightZigZag, subtreeMax)

        return dfs(root).subtreeMax
