"""
https://leetcode.com/problems/merge-two-sorted-lists/

Runtime: 36 ms, faster than 95.31% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 31.83% of Python3 online submissions for Merge Two Sorted Lists.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
