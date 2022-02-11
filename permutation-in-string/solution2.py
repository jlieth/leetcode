"""
https://leetcode.com/problems/permutation-in-string/

Runtime: 65 ms, faster than 89.45% of Python3 online submissions for Permutation in String.
Memory Usage: 13.8 MB, less than 99.16% of Python3 online submissions for Permutation in String.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        c1 = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}
        for char in s1:
            c1[char] += 1

        c2 = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}
        for idx, char in enumerate(s2):
            # add count for current char
            c2[char] += 1

            # remove count for char that fell out of window
            if idx >= length:
                c2[s2[idx - length]] -= 1

            # compare counters
            if c1 == c2:
                return True

        return False
