"""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Recursive:
Runtime: 61 ms, faster than 76.18% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 16.2 MB, less than 65.21% of Python3 online submissions for N-ary Tree Preorder Traversal.

Iterative:
Runtime: 49 ms, faster than 96.57% of Python3 online submissions for N-ary Tree Preorder Traversal.
Memory Usage: 16.1 MB, less than 80.97% of Python3 online submissions for N-ary Tree Preorder Traversal.
"""
from collections import deque
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        if root is None:
            return []

        # return self.preorder_recursive(root)
        return self.preorder_iterative(root)

    def preorder_recursive(self, root: "Node") -> List[int]:
        result = [root.val]
        for child in root.children:
            result += self.preorder(child)

        return result

    def preorder_iterative(self, root: "Node") -> List[int]:
        result = []
        q = deque([root])
        while len(q) > 0:
            node = q.popleft()
            result.append(node.val)
            q.extendleft(node.children[::-1])  # reverse to preserve order of children
        return result
