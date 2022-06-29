"""
https://leetcode.com/problems/fibonacci-number/

bottom up:
Runtime: 36 ms, faster than 84.33% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.9 MB, less than 54.29% of Python3 online submissions for Fibonacci Number.

top down:
Runtime: 39 ms, faster than 76.82% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.9 MB, less than 54.29% of Python3 online submissions for Fibonacci Number.
"""
from functools import cache


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        # return self.bottomUp(n)
        return self.topDown(n)

    def bottomUp(self, n: int) -> int:
        nums = [0] * (n + 1)
        nums[0] = 0
        nums[1] = 1
        for i in range(2, n + 1):
            nums[i] = nums[i - 1] + nums[i - 2]

        return nums[n]

    @cache
    def topDown(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.topDown(n - 1) + self.topDown(n - 2)
