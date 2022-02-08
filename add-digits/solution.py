"""
https://leetcode.com/problems/add-digits

Runtime: 40 ms, faster than 51.49% of Python3 online submissions for Add Digits.
Memory Usage: 13.9 MB, less than 91.66% of Python3 online submissions for Add Digits.
"""


class Solution:
    def addDigits(self, num: int) -> int:
        result = num
        while result >= 10:
            result = self.addDigitsOnce(result)
        return result

    def addDigitsOnce(self, num: int) -> int:
        result = 0
        while num > 0:
            digit = num % 10
            result += digit
            num = int(num / 10)
        return result
