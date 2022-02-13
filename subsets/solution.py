"""
https://leetcode.com/problems/subsets/

Runtime: 44 ms, faster than 53.44% of Python3 online submissions for Subsets.
Memory Usage: 14.2 MB, less than 69.11% of Python3 online submissions for Subsets.
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        bit manipulation:
            interpret items in powerset as binary numbers. the exponent of
            every set bit corresponds to the index in nums of the
            numbers contained in this item.
        example:
            nums = [2, 4, 6]
            powerset = [
                [],         # 0b000
                [2],        # 0b001 (contains nums[0])
                [4],        # 0b010 (contains nums[1])
                [2,4],      # 0b011 (contains nums[0], nums[1])
                [6],        # 0b100 (contains nums[2])
                [2,6],      # 0b101 (contains nums[0], nums[2])
                [4,6],      # 0b110 (contains nums[1], nums[2])
                [2,4,6],    # 0b111 (contains nums[0], nums[1], nums[2])
            ]
        """
        result = []
        upper_bound = 2 ** len(nums)

        for n in range(0, upper_bound):
            result.append([])
            idx = 0
            while n > 0:
                bit = n % 2
                if bit == 1:
                    result[-1].append(nums[idx])
                idx += 1
                n = n >> 1

        return result
