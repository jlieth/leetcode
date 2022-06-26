"""
https://leetcode.com/problems/binary-search/

Runtime: 249 ms, faster than 94.47% of Python3 online submissions for Binary Search.
Memory Usage: 15.4 MB, less than 71.43% of Python3 online submissions for Binary Search.
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int, offset: int = 0) -> int:
        if len(nums) == 0:
            return -1

        middle_idx = len(nums) // 2
        middle = nums[middle_idx]

        if target == middle:
            return offset + middle_idx
        if target < middle:
            return self.search(nums[:middle_idx], target, offset)
        else:
            return self.search(nums[middle_idx + 1 :], target, offset + middle_idx + 1)
