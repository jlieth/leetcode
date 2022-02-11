"""
https://leetcode.com/problems/permutation-in-string/

Runtime: 1408 ms, faster than 31.67% of Python3 online submissions for Permutation in String.
Memory Usage: 14 MB, less than 83.82% of Python3 online submissions for Permutation in String.
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        end_idx = len(s2) - length + 1
        c1 = Counter(s1)
        for idx in range(0, end_idx):
            substring = s2[idx : idx + length]

            if idx > 0 and substring[-1] == s2[idx - 1]:
                continue

            c2 = Counter(substring)
            if c1 == c2:
                return True

        return False
