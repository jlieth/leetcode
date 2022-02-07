"""
https://leetcode.com/problems/find-the-difference

Runtime: 36 ms, faster than 76.52% of Python3 online submissions for Find the Difference.
Memory Usage: 14 MB, less than 88.02% of Python3 online submissions for Find the Difference.
"""
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = Counter(t) - Counter(s)
        return list(diff)[0]
