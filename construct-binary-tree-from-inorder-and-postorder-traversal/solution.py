"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Runtime: 214 ms, faster than 35.20% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 89.2 MB, less than 8.04% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder) == 0:
            return None

        val = postorder[-1]
        head = TreeNode(val)
        idx = inorder.index(val)

        left_inorder = inorder[:idx]
        left_postorder = postorder[: len(left_inorder)]
        head.left = self.buildTree(left_inorder, left_postorder)

        right_inorder = inorder[idx + 1 :]
        right_postorder = postorder[len(left_inorder) : -1]
        head.right = self.buildTree(right_inorder, right_postorder)

        return head
