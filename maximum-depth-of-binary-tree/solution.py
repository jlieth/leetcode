"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Runtime: 40 ms, faster than 89.57% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.5 MB, less than 8.18% of Python3 online submissions for Maximum Depth of Binary Tree.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth: int = 0) -> int:
        if root is None:
            return depth

        return max(
            self.maxDepth(root.left, depth + 1), self.maxDepth(root.right, depth + 1)
        )
