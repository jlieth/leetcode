"""
https://leetcode.com/problems/middle-of-the-linked-list/

Runtime: 26 ms, faster than 98.30% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.9 MB, less than 54.69% of Python3 online submissions for Middle of the Linked List.
"""
from math import floor
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # count all nodes
        num_nodes = 0
        node = head
        while node is not None:
            num_nodes += 1
            node = node.next

        # calculate index of middle node
        middle = floor(num_nodes / 2)

        # go to next node the number of times of the middle index (thus
        # arriving at the node with the middle index)
        node = head
        for _ in range(middle):
            node = node.next

        return node
