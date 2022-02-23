"""
https://leetcode.com/problems/clone-graph/

Runtime: 46 ms, faster than 63.44% of Python3 online submissions for Clone Graph.
Memory Usage: 14.6 MB, less than 34.46% of Python3 online submissions for Clone Graph.
"""
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.nodes = {}

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return

        clone = Node(node.val)
        self.nodes[clone.val] = clone

        for x in node.neighbors:
            if x.val in self.nodes:
                clone.neighbors.append(self.nodes[x.val])
            else:
                clone.neighbors.append(self.cloneGraph(x))

        return clone
