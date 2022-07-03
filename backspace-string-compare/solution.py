"""
https://leetcode.com/problems/backspace-string-compare/

Runtime: 42 ms, faster than 64.89% of Python3 online submissions for Backspace String Compare.
Memory Usage: 13.9 MB, less than 73.85% of Python3 online submissions for Backspace String Compare.
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_clean = ""
        t_clean = ""

        for char in s:
            if char == "#":
                s_clean = s_clean[:-1]
            else:
                s_clean += char

        for char in t:
            if char == "#":
                t_clean = t_clean[:-1]
            else:
                t_clean += char

        return s_clean == t_clean
