# 2236. Root Equals Sum of Children - Easy

# You are given the root of a binary tree that consists of exactly 3 nodes: the root, its left child, and its right child.

# Return true if the value of the root is equal to the sum of the values of its two children, or false otherwise.

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:

        if root.val - (root.left.val + root.right.val) == 0:
            return True
        else:
            return False
