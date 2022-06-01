"""
https://leetcode.com/problems/running-sum-of-1d-array/

Runtime: 41 ms, faster than 86.96% of Python3 online submissions for Running Sum of 1d Array.
Memory Usage: 14.1 MB, less than 73.38% of Python3 online submissions for Running Sum of 1d Array.
"""
from itertools import accumulate
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))

