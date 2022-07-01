"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Runtime: 452 ms, faster than 22.68% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 15.4 MB, less than 33.10% of Python3 online submissions for Find All Anagrams in a String.
"""
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        result = []
        target = Counter(p)
        substring = Counter(s[0 : len(p)])

        if substring == target:
            result.append(0)

        start = 1
        end = len(p)
        while end < len(s):
            substring.subtract(s[start - 1])  # remove last char from counter
            substring.update(s[end])  # add next char
            if substring == target:
                result.append(start)
            start += 1
            end += 1
        return result
