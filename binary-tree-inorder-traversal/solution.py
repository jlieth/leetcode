"""
https://leetcode.com/problems/binary-tree-inorder-traversal/

Runtime: 28 ms, faster than 92.84% of Python3 online submissions for Binary Tree Inorder Traversal.
Memory Usage: 13.9 MB, less than 88.64% of Python3 online submissions for Binary Tree Inorder Traversal.

Note: The problem didn't require an iterative solution but recommended
implementing one anyway because the recursive solution is trivial.
Results above are for the iterative solution.
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.iterative(root)

    def iterative(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        while True:
            if current:
                stack.append(current)
                current = current.left
            elif len(stack) > 0:
                node = stack.pop()
                result.append(node.val)
                current = node.right
            else:
                break

        return result

    def recursive(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return self.recursive(root.left) + [root.val] + self.recursive(root.right)
