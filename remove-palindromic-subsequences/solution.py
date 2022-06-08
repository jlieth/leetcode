"""
https://leetcode.com/problems/remove-palindromic-subsequences/

Runtime: 31 ms, faster than 83.78% of Python3 online submissions for Remove Palindromic Subsequences.
Memory Usage: 13.8 MB, less than 96.22% of Python3 online submissions for Remove Palindromic Subsequences.
"""


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        return 2

