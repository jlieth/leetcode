"""
https://leetcode.com/problems/remove-k-digits/

Runtime: 728 ms, faster than 5.07% of Python3 online submissions for Remove K Digits.
Memory Usage: 14.2 MB, less than 67.26% of Python3 online submissions for Remove K Digits.
"""
from typing import Tuple


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"

        # remove out-of-order digits from input string until no further
        # digits could or should be removed
        result = num
        total_removed = 0
        while True:
            removed, result = self.remove_out_of_order(result)
            if removed:
                total_removed += 1
            if not removed or total_removed == k:
                break

        # if we haven't removed enough digits yet, cut off the digits from the end
        missing = k - total_removed
        if missing > 0:
            result = result[:-missing]

        return str(int(result))

    def remove_out_of_order(self, num: str) -> Tuple[bool, str]:
        """
        finds and removes the first digit in the input string that is
        greater than the digit that follows it
        """
        result = ""
        removed = False
        for idx, digit in enumerate(num):
            # don't check last digit in string and just add it
            if idx == len(num) - 1:
                result += digit
                break

            # found the digit: add remaining digits to result and break
            if digit > num[idx + 1]:
                removed = True
                result += num[idx + 1 :]
                break

            result += digit

        return removed, result
