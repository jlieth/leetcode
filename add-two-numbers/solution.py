"""
https://leetcode.com/problems/add-two-numbers/

Runtime: 88 ms, faster than 45.68% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14 MB, less than 90.09% of Python3 online submissions for Add Two Numbers.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def whole(l: ListNode, i=0):
    depth = 0
    sum_ = l.val
    next_ = l.next
    while next_ is not None:
        depth += 1
        sum_ += next_.val * 10**depth
        next_ = next_.next
    return sum_


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1 = whole(l1)
        v2 = whole(l2)
        sum_ = v1 + v2
        num_digits = len(str(sum_))

        next_ = None
        for i in range(num_digits, 0, -1):
            val = int(sum_ % 10**i / 10 ** (i - 1))
            node = ListNode(val)
            node.next = next_
            next_ = node

        return next_
