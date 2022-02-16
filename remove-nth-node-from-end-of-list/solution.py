"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Runtime: 20 ms, faster than 99.88% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 14.1 MB, less than 64.38% of Python3 online submissions for Remove Nth Node From End of List.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node, _ = self.rem(head, n)
        return node

    def rem(self, node: ListNode, n: int):
        if not node:
            parent_height = 1
            return None, parent_height

        child, height = self.rem(node.next, n)
        node.next = child

        if height == n:
            return child, height + 1
        else:
            return node, height + 1
