"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Runtime: 4496 ms, faster than 7.45% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 15.1 MB, less than 77.41% of Python3 online submissions for Find All Anagrams in a String.
"""

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p)
        result = []
        char_freq = Counter(p)

        skipnext = False
        added = False
        for i in range(0, len(s) - length + 1):
            if skipnext:
                if added:
                    result.append(i)
                skipnext = False
                continue
            substring = s[i : i + length]

            if Counter(substring) == char_freq:
                result.append(i)
                added = True
            else:
                added = False

            try:
                if substring[0] == s[i + length]:
                    skipnext = True
            except IndexError:
                pass

        return result
