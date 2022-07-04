"""
https://leetcode.com/problems/top-k-frequent-words/

Runtime: 106 ms, faster than 21.90% of Python3 online submissions for Top K Frequent Words.
Memory Usage: 13.9 MB, less than 64.70% of Python3 online submissions for Top K Frequent Words.
"""
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        l = sorted(c.items(), key=lambda x: (-x[1], x[0]))
        return [x[0] for x in l[:k]]
