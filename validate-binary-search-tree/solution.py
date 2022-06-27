"""
https://leetcode.com/problems/validate-binary-search-tree/

Runtime: 56 ms, faster than 71.52% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 17.1 MB, less than 13.91% of Python3 online submissions for Validate Binary Search Tree.
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(
        self, root: Optional[TreeNode], min_: int = -(2**31) - 1, max_: int = 2**31
    ) -> bool:
        if not root:
            return True

        valid = min_ < root.val < max_
        if root.left:
            valid &= root.left.val < root.val
            valid &= self.isValidBST(root.left, min_, root.val)
        if root.right:
            valid &= root.right.val > root.val
            valid &= self.isValidBST(root.right, root.val, max_)
        return valid
