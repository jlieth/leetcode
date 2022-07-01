"""
https://leetcode.com/problems/unique-paths/

Runtime: 27 ms, faster than 98.09% of Python3 online submissions for Unique Paths.
Memory Usage: 14.8 MB, less than 6.95% of Python3 online submissions for Unique Paths.
"""
from functools import cache


class Solution:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:  # only one unique way for edges
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
