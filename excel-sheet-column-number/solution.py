"""
https://leetcode.com/problems/excel-sheet-column-number/

Runtime: 32 ms, faster than 90.14% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.8 MB, less than 83.72% of Python3 online submissions for Excel Sheet Column Number.
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i, char in enumerate(columnTitle[::-1]):
            val = ord(char) - 64
            result += val * 26**i
        return result
