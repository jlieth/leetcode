"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Runtime: 5648 ms, faster than 7.17% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 113.4 MB, less than 10.05% of Python3 online submissions for Find All Anagrams in a String.
"""

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        length = len(p)
        result = []
        char_freq = Counter(p)
        cache = {}

        for i in range(0, len(s) - length + 1):
            substring = s[i : i + length]
            val = cache.get(substring)
            if val is None:
                if Counter(substring) == char_freq:
                    result.append(i)
                    cache[substring] = True
                else:
                    cache[substring] = False

            else:
                if val:
                    result.append(i)

        return result
