"""
https://leetcode.com/problems/last-stone-weight/

Runtime: 32 ms, faster than 93.00% of Python3 online submissions for Last Stone Weight.
Memory Usage: 13.8 MB, less than 62.26% of Python3 online submissions for Last Stone Weight.
"""
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = list(-x for x in stones)
        heapify(h)

        while len(h) >= 2:
            y = -1 * heappop(h)
            x = -1 * heappop(h)
            if not x == y:
                heappush(h, -1 * (y - x))

        last = 0
        if len(h) == 1:
            last = -1 * heappop(h)

        return last
