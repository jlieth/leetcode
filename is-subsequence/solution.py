"""
https://leetcode.com/problems/is-subsequence/

Runtime: 28 ms, faster than 96.54% of Python3 online submissions for Is Subsequence.
Memory Usage: 14.1 MB, less than 55.23% of Python3 online submissions for Is Subsequence.
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        idx = 0
        for char in t:
            if char == s[idx]:
                idx += 1
            if idx == len(s):
                return True

        return False
