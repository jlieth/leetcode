"""
https://leetcode.com/problems/two-sum/

Runtime: 101 ms, faster than 51.13% of Python3 online submissions for Two Sum.
Memory Usage: 15.2 MB, less than 61.08% of Python3 online submissions for Two Sum.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in d:
                return [d[complement], i]
            d[x] = i
