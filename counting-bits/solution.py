"""
https://leetcode.com/problems/counting-bits/

Runtime: 85 ms, faster than 85.42% of Python3 online submissions for Counting Bits.
Memory Usage: 20.8 MB, less than 87.66% of Python3 online submissions for Counting Bits.
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(x).count("1") for x in range(n + 1)]
