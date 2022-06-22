"""
https://leetcode.com/problems/reverse-linked-list/

Runtime: 55 ms, faster than 45.79% of Python3 online submissions for Reverse Linked List.
Memory Usage: 20.5 MB, less than 9.21% of Python3 online submissions for Reverse Linked List.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(
        self, node: Optional[ListNode], parent: Optional[ListNode] = None
    ) -> Optional[ListNode]:
        if node is None:
            return parent

        child = node.next
        node.next = parent
        return self.reverseList(child, node)
