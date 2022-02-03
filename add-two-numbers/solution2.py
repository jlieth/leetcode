"""
https://leetcode.com/problems/add-two-numbers/

Runtime: 80 ms, faster than 53.64% of Python3 online submissions for Add Two Numbers.
Memory Usage: 13.8 MB, less than 99.17% of Python3 online submissions for Add Two Numbers.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.create_node(l1, l2)

    def create_node(
        self,
        l1: Optional[ListNode] = None,
        l2: Optional[ListNode] = None,
        overflow: int = 0,
    ) -> ListNode:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        sum_ = v1 + v2 + overflow
        val = sum_ % 10
        overflow = int(sum_ / 10)
        node = ListNode(val)

        next1 = l1.next if l1 else None
        next2 = l2.next if l2 else None

        if next1 or next2 or overflow > 0:
            next_ = self.create_node(next1, next2, overflow)
            node.next = next_
        return node
