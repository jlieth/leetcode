"""
https://leetcode.com/problems/transpose-matrix/

Runtime: 80 ms, faster than 76.67% of Python3 online submissions for Transpose Matrix.
Memory Usage: 14.7 MB, less than 55.33% of Python3 online submissions for Transpose Matrix.
"""
from itertools import zip_longest
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [list(row) for row in zip_longest(*matrix)]

