"""
https://leetcode.com/problems/symmetric-tree/

Runtime: 45 ms, faster than 61.04% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14 MB, less than 60.88% of Python3 online submissions for Symmetric Tree.
"""
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        create lists with values of both sides.
        for the right list, switch values for left and right children.
        compare lists.
        """
        left = []
        right = []

        # left
        queue = deque([root.left])
        while len(queue):
            current = queue.popleft()
            if not current:
                left.append(None)
                continue

            left.append(current.val)
            queue.append(current.left)
            queue.append(current.right)

        # right
        queue = deque([root.right])
        while len(queue):
            current = queue.popleft()
            if not current:
                right.append(None)
                continue

            right.append(current.val)
            queue.append(current.right)
            queue.append(current.left)

        return left == right
