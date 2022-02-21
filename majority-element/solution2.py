"""
https://leetcode.com/problems/majority-element/

Runtime: 192 ms, faster than 64.27% of Python3 online submissions for Majority Element.
Memory Usage: 15.5 MB, less than 81.72% of Python3 online submissions for Majority Element.

Note: Follow-up question in the original problem required a solution
with linear time and O(1) space. This is the Boyer-Moore majority
vote algorithm.
https://en.wikipedia.org/wiki/Boyer-Moore_majority_vote_algorithm
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        current = None
        for n in nums:
            if count == 0:
                current = n
                count = 1
            elif n == current:
                count += 1
            else:
                count -= 1

        return current
