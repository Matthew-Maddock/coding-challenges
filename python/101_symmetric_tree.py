# 101. Symmetric Tree - Easy

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Example 1:


# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        stack = []
        stack.append(root.right)
        stack.append(root.left)
        
        while(stack):
            leftNode = stack.pop()
            rightNode = stack.pop()
            
            if leftNode == None and rightNode == None:
                continue
                
            if leftNode == None or rightNode == None or (leftNode.val != rightNode.val):
                return False
            
            stack.append(leftNode.left)
            stack.append(rightNode.right)
            
            stack.append(leftNode.right)
            stack.append(rightNode.left)
            
        return True