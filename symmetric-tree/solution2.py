"""
https://leetcode.com/problems/symmetric-tree/

Runtime: 32 ms, faster than 94.59% of Python3 online submissions for Symmetric Tree.
Memory Usage: 14.1 MB, less than 60.88% of Python3 online submissions for Symmetric Tree.
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
        if not root:
            return True

        queue = deque()
        queue.append((root.left, root.right))
        while len(queue):
            left, right = queue.popleft()

            # if both are None, continue
            if not left and not right:
                continue

            # if only one of them is None, return False
            if (left and not right) or (right and not left):
                return False

            # if their values are different, return False
            if not left.val == right.val:
                return False

            # append children to stack
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True
