"""
https://leetcode.com/problems/contiguous-array

Runtime: 951 ms, faster than 54.46% of Python3 online submissions for Contiguous Array.
Memory Usage: 23.3 MB, less than 5.28% of Python3 online submissions for Contiguous Array.
"""
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result = 0

        # keys: number of ones more than zeroes
        # values: list of indices where it applies
        hashtable = {}

        ones = 0
        for idx, x in enumerate(nums):
            ones += x
            zeroes = (idx + 1) - ones
            more_ones = ones - zeroes

            # update result if same number of ones and zeroes
            if more_ones == 0:
                result = idx + 1

            try:
                hashtable[more_ones].append(idx)
            except KeyError:
                hashtable[more_ones] = [idx]

        # all pairs  of items in each indices list in the hashtable
        # give a contiguous array: if nums[10] has 3 more ones than zeroes
        # and so does nums[3], the array nums[4:11] has the same number
        # of ones and zeroes
        for indices in hashtable.values():
            length = indices[-1] - indices[0]
            result = max(result, length)

        return result
