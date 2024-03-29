# 652. Find Duplicate Subtrees - Medium

# Given the root of a binary tree, return all duplicate subtrees.

# For each kind of duplicate subtrees, you only need to return the root node of any one of them.

# Two trees are duplicate if they have the same structure with the same node values.

# Example 1:

# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        res = []

        tree_map = {}

        def dfs(node, path):
            if not node:
                return "#"

            path += ",".join([str(node.val), dfs(node.left, path), dfs(node.right, path)])

            if path in tree_map:
                tree_map[path] += 1

                if tree_map[path] == 2:
                    res.append(node)

            else:
                tree_map[path] = 1

            return path

        dfs(root, "")

        return res
