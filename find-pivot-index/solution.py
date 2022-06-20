"""
https://leetcode.com/problems/find-pivot-index/

Runtime: 159 ms, faster than 89.63% of Python3 online submissions for Find Pivot Index.
Memory Usage: 15.2 MB, less than 92.60% of Python3 online submissions for Find Pivot Index.
"""
from itertools import accumulate
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = list(accumulate(nums))
        length = len(nums)

        for idx in range(length):
            # get left sum
            if idx == 0:
                left_sum = 0
            else:
                left_sum = prefix_sum[idx - 1]

            # get right sum
            if idx == length - 1:
                right_sum = 0
            else:
                right_sum = prefix_sum[length - 1] - prefix_sum[idx]

            if left_sum == right_sum:
                return idx

        return -1
