"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Runtime: 196 ms, faster than 51.27% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 88.8 MB, less than 10.03% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        val = preorder[0]
        head = TreeNode(val)
        idx = inorder.index(val)

        left_inorder = inorder[:idx]
        left_preorder = preorder[1 : len(left_inorder) + 1]
        head.left = self.buildTree(left_preorder, left_inorder)

        right_inorder = inorder[idx + 1 :]
        right_preorder = preorder[len(left_inorder) + 1 :]
        head.right = self.buildTree(right_preorder, right_inorder)

        return head
