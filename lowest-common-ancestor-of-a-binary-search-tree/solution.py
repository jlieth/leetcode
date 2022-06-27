"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Runtime: 86 ms, faster than 86.50% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 18.8 MB, less than 22.19% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        lesser = min(p.val, q.val)
        greater = max(p.val, q.val)

        if lesser <= root.val <= greater:
            return root

        if root.val > greater:  # search left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < lesser:  # search right subtree
            return self.lowestCommonAncestor(root.right, p, q)
