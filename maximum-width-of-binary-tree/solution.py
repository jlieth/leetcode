"""
https://leetcode.com/problems/maximum-width-of-binary-tree/

Runtime: 52 ms, faster than 71.17% of Python3 online submissions for Maximum Width of Binary Tree.
Memory Usage: 15.8 MB, less than 24.10% of Python3 online submissions for Maximum Width of Binary Tree.
"""
from collections import defaultdict, deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)
        queue = deque([(root, 0, 1)])
        while len(queue):
            current, lvl, idx = queue.popleft()
            if not current:
                continue

            levels[lvl].append(idx)

            # calculate idx of children
            lvl_start_idx = 2**lvl
            nodes_before = idx - lvl_start_idx
            children_start_idx = 2 ** (lvl + 1) + 2 * nodes_before

            queue.append((current.left, lvl + 1, children_start_idx))
            queue.append((current.right, lvl + 1, children_start_idx + 1))

        longest = max(x[-1] - x[0] for x in levels.values()) + 1
        return longest
