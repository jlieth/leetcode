"""
https://leetcode.com/problems/merge-k-sorted-lists

Runtime: 7300 ms
Memory: 25.9 MB

Note: This solution is bad. I just went with the naive approach
first to see if it can beat the time limit. It did, but only once.
Every other submission I did after the first ended in time limit
exceeded. So this is kind of a fake solution and shouldn't have
made it through the tests in the first place but somehow did.
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        result = lists[0]
        for l in lists[1:]:
            result = self.merge_sort(result, l)
        return result

    def merge_sort(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if list1 and not list2:
            return list1
        if not list1 and list2:
            return list2

        if list1.val < list2.val:
            list1.next = self.merge_sort(list1.next, list2)
            return list1
        else:
            list2.next = self.merge_sort(list2.next, list1)
            return list2
