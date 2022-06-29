"""
https://leetcode.com/problems/climbing-stairs/

bottom up:
Runtime: 30 ms, faster than 93.00% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.8 MB, less than 95.99% of Python3 online submissions for Climbing Stairs.

top down:
Runtime: 29 ms, faster than 94.46% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.9 MB, less than 11.61% of Python3 online submissions for Climbing Stairs.
"""
from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        # return self.bottomUp(n)
        return self.topDown(n)

    def bottomUp(self, n: int) -> int:
        nums = [0] * (n + 1)
        nums[1] = 1
        nums[2] = 2
        for i in range(3, n + 1):
            nums[i] = nums[i - 1] + nums[i - 2]

        return nums[n]

    @cache
    def topDown(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.topDown(n - 1) + self.topDown(n - 2)
