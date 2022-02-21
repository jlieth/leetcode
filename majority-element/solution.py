"""
https://leetcode.com/problems/majority-element/

Runtime: 170 ms, faster than 80.91% of Python3 online submissions for Majority Element.
Memory Usage: 15.5 MB, less than 81.81% of Python3 online submissions for Majority Element.
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]
