# 106. Construct Binary Tree from Inorder and Postorder Traversal - Medium

# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder
# traversal of the same tree, construct and return the binary tree.

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None

        value = postorder[-1]
        root = TreeNode(value)
        mid = inorder.index(value)

        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1 :], postorder[mid:-1])

        return root
