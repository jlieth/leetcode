"""
https://leetcode.com/problems/delete-and-earn/

Runtime: 124 ms, faster than 18.82% of Python3 online submissions for Delete and Earn.
Memory Usage: 14.2 MB, less than 85.04% of Python3 online submissions for Delete and Earn.
"""
from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = Counter(nums)
        nums = sorted(list(set(nums)))

        points = []
        max_points = 0

        for idx in range(len(nums)):
            n = nums[idx]

            # find the index of the first number before n that is eligible
            try:
                # found: eligible number is previous to first illegal number
                illegal_idx = nums.index(n - 1)
                prev_idx = illegal_idx - 1
            except ValueError:
                # no illegal numbers found: eligible number is immediately previous
                prev_idx = idx - 1

            if prev_idx < 0:
                p = n * counts[n]
            else:
                p = n * counts[n] + max(points[: prev_idx + 1])

            max_points = max(max_points, p)
            points.append(p)

        return max_points
