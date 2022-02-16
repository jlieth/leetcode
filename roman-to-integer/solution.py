"""
https://leetcode.com/problems/roman-to-integer/

Runtime: 50 ms, faster than 75.55% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.9 MB, less than 93.95% of Python3 online submissions for Roman to Integer.
"""


class Solution:
    VALS = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        n = 0
        idx = 0
        while idx < len(s):
            two_char = s[idx : idx + 2]
            if two_char in self.VALS:
                n += self.VALS[two_char]
                idx += 2
            else:
                n += self.VALS[s[idx]]
                idx += 1

        return n
