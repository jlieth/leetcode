"""
https://leetcode.com/problems/path-sum/

Runtime: 40 ms, faster than 95.22% of Python3 online submissions for Path Sum.
Memory Usage: 15.1 MB, less than 32.24% of Python3 online submissions for Path Sum.
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        q = deque()
        q.append((root, targetSum))
        while len(q):
            current, target = q.popleft()
            target -= current.val

            # is this a leaf?
            if not (current.left or current.right):
                if target == 0:
                    return True
                continue

            if current.left:
                q.append((current.left, target))
            if current.right:
                q.append((current.right, target))

        return False
