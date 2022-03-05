"""
https://leetcode.com/problems/delete-and-earn/

Runtime: 4179 ms, faster than 5.02% of Python3 online submissions for Delete and Earn.
Memory Usage: 16.2 MB, less than 6.25% of Python3 online submissions for Delete and Earn.
"""
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def dp(idx: int) -> int:
            n = nums[idx]

            if idx in memo:
                return memo[idx]

            result = n + max(
                [0] + [dp(prev) for prev in range(0, idx) if not nums[prev] == n - 1]
            )
            memo[idx] = result
            return result

        nums.sort()
        memo = {}
        max_points = 0
        for idx in range(len(nums)):
            max_points = max(max_points, dp(idx))

        return max_points
