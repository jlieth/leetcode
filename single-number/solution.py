"""
https://leetcode.com/problems/single-number/

Runtime: 147 ms, faster than 67.83% of Python3 online submissions for Single Number.
Memory Usage: 16.8 MB, less than 10.39% of Python3 online submissions for Single Number.
"""
from functools import reduce
from operator import xor
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
