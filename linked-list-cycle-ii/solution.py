"""
https://leetcode.com/problems/linked-list-cycle-ii/

Runtime: 42 ms, faster than 99.65% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.7 MB, less than 23.09% of Python3 online submissions for Linked List Cycle II.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = {}
        node = head
        while node is not None:
            if visited.get(id(node), False):
                return node
            visited[id(node)] = True
            node = node.next
        return None
