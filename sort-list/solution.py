"""
https://leetcode.com/problems/sort-list/

Runtime: 264 ms, faster than 88.12% of Python3 online submissions for Sort List.
Memory Usage: 35.7 MB, less than 19.83% of Python3 online submissions for Sort List.
"""
from heapq import heappush, heappop
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = []
        count = 0
        while head:
            heappush(h, (-head.val, count, head))
            head = head.next
            count += 1

        current = None
        for _ in range(len(h)):
            child = current
            current = heappop(h)[2]
            current.next = child

        return current
