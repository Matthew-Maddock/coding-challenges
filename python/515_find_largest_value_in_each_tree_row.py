# 515. Find Largest Value in Each Tree Row - Medium

# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Example 1:

# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# Example 2:

# Input: root = [1,2,3]
# Output: [1,3]
import collections
import math
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        q = collections.deque([root])

        while q:
            maxi = -math.inf
            for _ in range(len(q)):
                root = q.popleft()
                maxi = max(maxi, root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            ans.append(maxi)

        return ans
