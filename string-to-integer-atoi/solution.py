"""
https://leetcode.com/problems/string-to-integer-atoi/

Runtime: 37 ms, faster than 70.23% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.8 MB, less than 96.72% of Python3 online submissions for String to Integer (atoi).
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        int_as_str = "0"

        s = s.lstrip(" ")
        if len(s) == 0:
            return 0

        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]

        for char in s:
            if not char.isdigit():
                break

            int_as_str += char

        i = int(int_as_str) * sign

        if i < -(2**31):
            i = -(2**31)
        if i > 2**31 - 1:
            i = 2**31 - 1

        return i
