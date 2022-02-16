"""
https://leetcode.com/problems/palindrome-number/

Runtime: 91 ms, faster than 45.34% of Python3 online submissions for Palindrome Number.
Memory Usage: 13.9 MB, less than 88.92% of Python3 online submissions for Palindrome Number.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
