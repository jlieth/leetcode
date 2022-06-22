"""
https://leetcode.com/problems/range-sum-query-2d-immutable/

Runtime: 3452 ms, faster than 18.49% of Python3 online submissions for Range Sum Query 2D - Immutable.
Memory Usage: 49.7 MB, less than 5.00% of Python3 online submissions for Range Sum Query 2D - Immutable.
"""
from functools import cache
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])
        for row_idx in range(m):
            for col_idx in range(1, n):
                prev = self.matrix[row_idx][col_idx - 1]
                self.matrix[row_idx][col_idx] += prev

    @cache
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = 0
        for row in range(row1, row2 + 1):
            if col1 == 0:
                sum_ += self.matrix[row][col2]
            else:
                sum_ += self.matrix[row][col2] - self.matrix[row][col1 - 1]
        return sum_
