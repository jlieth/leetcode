"""
https://leetcode.com/problems/longest-palindrome/

Runtime: 40 ms, faster than 75.80% of Python3 online submissions for Longest Palindrome.
Memory Usage: 13.8 MB, less than 65.10% of Python3 online submissions for Longest Palindrome.
"""
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        length = 0
        for char, count in c.items():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1

        # is there a char left we can add in the middle?
        if length < len(s):
            length += 1

        return length
