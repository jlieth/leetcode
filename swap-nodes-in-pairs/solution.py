"""
https://leetcode.com/problems/swap-nodes-in-pairs/

Runtime: 40 ms, faster than 53.91% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 13.9 MB, less than 75.41% of Python3 online submissions for Swap Nodes in Pairs.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head

        return new_head
