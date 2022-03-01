"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Runtime: 32 ms, faster than 94.76% of Python3 online submissions for Binary Tree Level Order Traversal.
Memory Usage: 14.3 MB, less than 76.08% of Python3 online submissions for Binary Tree Level Order Traversal.
"""

from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        q = deque()
        q.append((root, 0))
        while len(q):
            current, lvl = q.popleft()
            if not current:
                continue
            levels[lvl].append(current.val)
            q.append((current.left, lvl + 1))
            q.append((current.right, lvl + 1))

        return [levels[x] for x in range(len(levels))]
